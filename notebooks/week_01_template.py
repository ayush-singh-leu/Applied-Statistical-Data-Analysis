import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Week 01 — Topic

    **Learning goals**

    - Add the first learning goal.
    - Add the second learning goal.
    - Add the third learning goal.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. Concept

    Explain the statistical idea here. Keep notation, intuition, and a
    concrete example close together.
    """)
    return


@app.cell
def _():
    # Replace this example with the week's data and analysis.
    example_values = [2, 4, 6, 8, 10]
    return (example_values,)


@app.cell
def _(example_values, mo):
    mo.md(f"The example mean is **{sum(example_values) / len(example_values):.1f}**.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Exercise

    Add a short student task here.

    <details>
    <summary>Show hint</summary>

    Add a useful hint here.

    </details>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Takeaways

    - Add the most important point from the week.
    - Add one common mistake to avoid.
    """)
    return


if __name__ == "__main__":
    app.run()
