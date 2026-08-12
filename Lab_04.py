import csv

ANY = "?"
NULL = "∅"


def covers(hypothesis, instance):
    return all(
        h == ANY or h == x
        for h, x in zip(hypothesis, instance)
    )


def more_general_or_equal(h1, h2):
    return all(
        a == ANY or a == b
        for a, b in zip(h1, h2)
    )


def minimal_generalization(s, instance):
    new_s = list(s)

    for i, value in enumerate(instance):
        if new_s[i] == NULL:
            new_s[i] = value
        elif new_s[i] != value:
            new_s[i] = ANY

    return tuple(new_s)


def minimal_specializations(g, instance, domains):
    specializations = []

    for i, value in enumerate(instance):
        if g[i] == ANY:
            for domain_value in domains[i]:
                if domain_value != value:
                    h = list(g)
                    h[i] = domain_value
                    specializations.append(tuple(h))

    return specializations


def remove_more_specific(hypotheses):
    result = set(hypotheses)

    for h1 in list(result):
        for h2 in list(result):
            if h1 != h2 and more_general_or_equal(h1, h2):
                result.discard(h2)

    return result


def remove_more_general(hypotheses):
    result = set(hypotheses)

    for h1 in list(result):
        for h2 in list(result):
            if h1 != h2 and more_general_or_equal(h1, h2):
                result.discard(h1)
                break

    return result


def format_hypothesis(h):
    return "<" + ", ".join(h) + ">"


def format_boundary(boundary):
    if not boundary:
        return "{ }"

    return "{ " + ", ".join(
        format_hypothesis(h) for h in sorted(boundary)
    ) + " }"


def candidate_elimination(data):

    attributes = ["Sky", "AirTemp", "Humidity", "Wind"]

    domains = [
        sorted({row[a] for row in data})
        for a in attributes
    ]

    # Most Specific Boundary
    S = {tuple([NULL] * len(attributes))}

    # Most General Boundary
    G = {tuple([ANY] * len(attributes))}

    print("=" * 72)
    print("CANDIDATE ELIMINATION ALGORITHM")
    print("=" * 72)

    print("\nInitial Boundaries:")
    print("S =", format_boundary(S))
    print("G =", format_boundary(G))

    for step, row in enumerate(data, start=1):

        instance = tuple(
            row[a] for a in attributes
        )

        target = row["EnjoySport"]

        print(f"\n{'-' * 72}")
        print(
            f"Step {step}: {row['Instance']} "
            f"-> {format_hypothesis(instance)} "
            f"Target = {target}"
        )
        print("-" * 72)

        # Positive example
        if target.lower() == "yes":

            # Remove hypotheses from G that do not cover instance
            G = {
                g for g in G
                if covers(g, instance)
            }

            new_S = set()

            for s in S:

                if covers(s, instance):
                    new_S.add(s)

                else:

                    generalized = minimal_generalization(
                        s,
                        instance
                    )

                    for g in G:

                        if more_general_or_equal(
                            g,
                            generalized
                        ):
                            new_S.add(generalized)
                            break

            S = remove_more_general(new_S)

        # Negative example
        else:

            # Remove S hypotheses that cover negative instance
            S = {
                s for s in S
                if not covers(s, instance)
            }

            new_G = set()

            for g in G:

                if not covers(g, instance):
                    new_G.add(g)

                else:

                    specializations = minimal_specializations(
                        g,
                        instance,
                        domains
                    )

                    for specialized in specializations:

                        if any(
                            more_general_or_equal(
                                specialized,
                                s
                            )
                            for s in S
                        ):
                            new_G.add(specialized)

            G = remove_more_specific(new_G)

        print("S =", format_boundary(S))
        print("G =", format_boundary(G))

    print(f"\n{'=' * 72}")
    print("FINAL VERSION SPACE BOUNDARIES")
    print("=" * 72)

    print("\nMost Specific Boundary (S):")
    print(format_boundary(S))

    print("\nMost General Boundary (G):")
    print(format_boundary(G))

    print("=" * 72)


def load_csv(filename="training_data.csv"):

    with open(
        filename,
        newline="",
        encoding="utf-8"
    ) as file:

        return list(csv.DictReader(file))


if __name__ == "__main__":

    training_data = load_csv()

    candidate_elimination(training_data)