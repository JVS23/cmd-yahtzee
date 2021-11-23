from invoke import task

# Tämän kanssa Windowsilla jotakin ongelmia, terminaalilla hankaluuksia lukea inputteja.
# normaalisti Pythonilla runnatessa toimii tosin normaalisti.


@task
def start(ctx):
    print("Starting app..")
    ctx.run("python3 src/main.py")


@task
def test(ctx):
    ctx.run("pytest src")

# @task
# def coverage-report(ctx):
