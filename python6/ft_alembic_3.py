from alchemy.elements import create_air


def main() -> None:
    print("=== Alembic 3 ===")
    print(
        "Accessing alchemy/elements.py using "
        "'from ... import ...' structure"
    )
    air_result = create_air()
    print(f"Testing create_air: {air_result}")


if __name__ == "__main__":
    main()
