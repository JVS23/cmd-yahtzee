from invoke import task

# startin kanssa Windowsilla jokin bugi, terminaalilla hankaluuksia lukea inputteja.
# normaalisti Pythonilla sekä Cubblilla runnatessa toimii tosin normaalisti.


@task
def start(ctx):
    print("Starting app..")
    ctx.run("python3 src/main.py")


@task
def test(ctx):
    ctx.run("pytest src")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
