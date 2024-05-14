import os
import random
import string

"""Generates a random string of lowercase letters."""


def generate_rand_string(length):
    characters = string.ascii_lowercase
    return ''.join(random.choice(characters) for _ in range(length))


def analyze_accessibility_results(results):
    total_violations, critical_violations, moderate_violations, serious_violations = count_violations(results)
    print("Total violations found:", total_violations)
    print("Critical violations:", critical_violations)
    print("Moderate violations:", moderate_violations)
    print("Serious violations:", serious_violations)

    print_violation_details(results)


def print_violation_details(results):
    if results:
        print("\nViolation details:")
        for i, violation in enumerate(results["violations"], start=1):
            print(f"\nViolation {i}:")
            print(f"Description: {violation['description']}")
            print(f"Impact: {violation['impact']}")
            print(f"Help: {violation['help']}")
            print(f"Help URL: {violation['helpUrl']}")


def count_violations(results):
    total_violations = len(results["violations"])
    critical_violations = sum(1 for violation in results["violations"] if violation["impact"] == "critical")
    moderate_violations = sum(1 for violation in results["violations"] if violation["impact"] == "moderate")
    serious_violations = sum(1 for violation in results["violations"] if violation["impact"] == "serious")
    return total_violations, critical_violations, moderate_violations, serious_violations
