import os
import sqlite3
from collections.abc import Callable
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import TypeAlias

import requests
from dotenv import load_dotenv

# GLOBAL VARIABLES
DB_DIR = Path(__file__).parent.parent.parent.resolve()

VALID_YEAR_RANGE = (2015, datetime.now().astimezone().year)
VALID_DAY_RANGE = (1, 25)

USER_AGENT = "github.com/Oligoflexia/advent-of-code by Oligoflexia"
AOC_URL = "https://adventofcode.com/{}/day/{}/input"

FormattedInput: TypeAlias = str | list[str] | float | list[float]

# ERROR MESSAGES
INPUT_TYPE_ERROR = "Param: '{}' must be of type '{}'!"
YEAR_RANGE_ERROR = """
    Param: 'year' must represent a valid year of AoC puzzles!
    Got: year='{}', but expected '{}' <= year <= '{}'!
    """
DAY_RANGE_ERROR = "Param: 'day' must be between 1 and 25!"
PARAM_ERROR = "Invalid param: '{}'!"
AOC_CONNECTION_ERROR = "Error fetching input str from AoC servers!"
DB_CREATION_ERROR = "Error creating db file at path: '{}'!"
DB_CONNECTION_ERROR = "Error connecting to db file at path: '{}'!"
DB_INIT_ERROR = "Error initializing db with schema!"
DB_RETRIEVAL_ERROR = "Error retrieving input string from db!"
DB_MISSING_RECORD_ERROR = "No input found for the given year and day values!"
DB_INSERTION_ERROR = "Error inserting input string into db!"
DB_KEY_ERROR = "An input with the same year '{}' and day '{}' values already exists in the database!"  # NOQA: E501
INPUT_RETRIEVAL_ERROR = "An error occured while trying to get the input!"



class InputFormat(Enum):
    @staticmethod
    def __get_single_str_input(input_str: str) -> str:
        return input_str

    @staticmethod
    def __get_split_str_input(input_str: str) -> list[str]:
        return list(input_str.splitlines())

    @staticmethod
    def __get_single_num_input(input_str: str) -> float:
        return float(input_str)

    @staticmethod
    def __get_split_num_input(input_str: str) -> list[float]:
        return [float(n) for n in input_str.splitlines()]

    SINGLE_STR = __get_single_str_input
    SPLIT_STR = __get_split_str_input
    SINGLE_NUM = __get_single_num_input
    SPLIT_NUM = __get_split_num_input


class InputHandler:
    def __init__(self, db_name: str = "inputs.db") -> None:
        self._db_name = db_name
        self._conn = None

    def __enter__(self) -> "InputHandler":
        self._conn = self.__get_db_connection(self._db_name)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:  #  NOQA: ANN001
        if self._conn:
            self._conn.close()

        # Allow exceptions to propagate by default
        return False

    @property
    def conn(self) -> sqlite3.Connection | None:
        return self._conn

    @staticmethod
    def get_input(
        year: int,
        day: int,
        db_name: str = "inputs.db",
        input_format: Callable = InputFormat.SINGLE_STR,
    ) -> FormattedInput:
        InputHandler.__validate_inputs(year=year, day=day, db_name=db_name)

        input_str = None

        with InputHandler(db_name) as handler:

            if handler.is_input_in_db(year, day):
                input_str = handler.get_input_from_db(year, day)
            else:
                input_str = handler.get_input_from_aoc(year, day)
                handler.insert_input_into_db(year, day, input_str)

        if not input_str:
            raise RuntimeError(INPUT_RETRIEVAL_ERROR)

        return input_format(input_str)

    @staticmethod
    def __validate_inputs(**kwargs: object) -> None:
        for kwarg in kwargs:
            match kwarg:
                case "year":
                    if not isinstance(kwargs["year"], int):
                        err_str = INPUT_TYPE_ERROR.format("year", "int")
                        raise TypeError(err_str)

                    if (kwargs["year"] < VALID_YEAR_RANGE[0]) or (
                        kwargs["year"] > VALID_YEAR_RANGE[1]
                    ):
                        err_str = YEAR_RANGE_ERROR.format(
                            kwargs["year"],
                            VALID_YEAR_RANGE[0],
                            VALID_YEAR_RANGE[1],
                        )
                        raise ValueError(err_str)

                case "day":
                    if not isinstance(kwargs["day"], int):
                        err_str = INPUT_TYPE_ERROR.format("day", "int")
                        raise TypeError(err_str)
                    if (kwargs["day"] < VALID_DAY_RANGE[0]) or (
                        kwargs["day"] > VALID_DAY_RANGE[1]
                    ):
                        err_str = DAY_RANGE_ERROR
                        raise ValueError(err_str)

                case "db_name":
                    if not isinstance(kwargs["db_name"], str):
                        err_str = INPUT_TYPE_ERROR.format("db_name", "str")
                        raise TypeError(err_str)

                case _:
                    err_str = PARAM_ERROR.format(kwarg)
                    raise ValueError(err_str)

    def get_input_from_aoc(self, year: int, day: int) -> str:
        load_dotenv()

        url = AOC_URL.format(year, day)
        cookies = {"session": os.getenv("SESSION_COOKIE", "")}
        headers = {"User-Agent": USER_AGENT}

        try:
            response = requests.get(
                url,
                headers=headers,
                cookies=cookies,
                timeout=5,
            )
        except requests.exceptions.RequestException as e:
            err_str = AOC_CONNECTION_ERROR
            raise ConnectionError(err_str) from e
        else:
            return response.text

    def __get_db_connection(self, db_name: str) -> sqlite3.Connection:
        sql_schema = """
            CREATE TABLE IF NOT EXISTS inputs (
                year INTEGER NOT NULL,
                day INTEGER NOT NULL,
                input_str TEXT,
                PRIMARY KEY (year, day)
             )
        """
        db_path = DB_DIR / db_name

        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(sql_schema)
            conn.commit()
        except sqlite3.Error as e:
            err_str = DB_CREATION_ERROR.format(db_path)
            raise ConnectionError(err_str) from e

        if not conn:
            err_str = DB_CONNECTION_ERROR.format(db_path)
            raise sqlite3.Error(err_str)

        return conn

    def get_input_from_db(self, year: int, day: int) -> str:
        sql_str = """
            SELECT input_str
            FROM inputs
            WHERE year = ? AND day = ?
        """

        if not self._conn:
            err_str = DB_CONNECTION_ERROR.format(DB_DIR / self._db_name)
            raise sqlite3.Error(err_str)

        try:
            cursor = self._conn.cursor()
            cursor.execute(sql_str, (year, day))
            result = cursor.fetchone()
        except sqlite3.Error as e:
            err_str = DB_RETRIEVAL_ERROR
            raise sqlite3.Error(err_str) from e
        else:
            if not result:
                err_str = DB_MISSING_RECORD_ERROR
                raise sqlite3.Error(err_str)
            return result[0]

    def insert_input_into_db(
        self,
        year: int,
        day: int,
        input_str: str,
    ) -> None:
        sql_str = """
            INSERT INTO inputs (year, day, input_str)
            VALUES (?, ?, ?)
        """

        if not self._conn:
            err_str = DB_CONNECTION_ERROR.format(DB_DIR / self._db_name)
            raise sqlite3.Error(err_str)

        try:
            cursor = self._conn.cursor()
            cursor.execute(sql_str, (year, day, input_str))
            self._conn.commit()
        except sqlite3.IntegrityError as e:
            err_str = DB_KEY_ERROR.format(year, day)
            raise sqlite3.Error(err_str) from e
        except sqlite3.Error as e:
            raise sqlite3.Error(DB_INSERTION_ERROR) from e

    def is_input_in_db(self, year: int, day: int) -> bool:
        sql_str = """
            SELECT count(*)
            from inputs
            WHERE year = ? AND day = ?
        """

        if not self._conn:
            err_str = DB_CONNECTION_ERROR.format(DB_DIR / self._db_name)
            raise sqlite3.Error(err_str)

        try:
            cursor = self._conn.cursor()
            cursor.execute(sql_str, (year, day))
            result = cursor.fetchone()
        except sqlite3.Error as e:
            err_str = "Error while checking if input exists in db!"
            raise sqlite3.Error(err_str) from e
        else:
            return result[0] > 0
