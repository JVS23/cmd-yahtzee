from invoke import task


@task
def start(ctx):
    print("Starting app..")
    ctx.run("python3 src/main.py")

# @task
# def test(ctx):

# @task
# def coverage-report(ctx):
