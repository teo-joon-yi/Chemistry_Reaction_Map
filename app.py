from flask import Flask, render_template, request, redirect, url_for, abort

validFunctionalGroups = ["alkanes", "alkenes", "arenes", "halogen-compounds", "alcohols", "phenols",
                         "ketones", "aldehydes", "carboxylic-acids", "acyl-halides", "esters",
                         "amines", "amides", "phenylamines", "nitriles", "cyanohydrins"]

def linkToFileName(inStr):
    inList = inStr.strip().split("-")
    for i in range(len(inList)):
        inList[i] = inList[i].capitalize()

    outFile = "reactionMap"
    outFile += " ".join(inList)
    outFile += ".html"
    return outFile

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def root():
    return redirect(url_for("home"))

@app.route("/home", methods = ["GET"])
def home():
    return render_template("reactionMapHome.html")

@app.route("/functional-groups", methods = ["GET"])
def functionalGroups():
    return render_template("reactionMapFunctionalGroups.html")

@app.route("/reagents-conditions", methods = ["GET"])
def reagentsConditions():
    return render_template("reactionMapReagentsConditions.html")

@app.route("/mechanisms", methods = ["GET"])
def mechanisms():
    return render_template("reactionMapMechanisms.html")

@app.route("/qa-tests", methods = ["GET"])
def qaTests():
    return render_template("reactionMapQATests.html")



@app.route("/functional-groups/<functionalGroup>", methods = ["GET"])
def getFunctionalGroup(functionalGroup):
    if functionalGroup not in validFunctionalGroups:
        abort(404)
    return render_template(linkToFileName(functionalGroup))

@app.route("/reagents-conditions/<reaction>", methods = ["GET"])
def getReagentCondition(reaction):
    return render_template(linkToFileName(reaction))

@app.route("/mechanisms/<mechanism>", methods = ["GET"])
def getMechanism(mechanism):
    return render_template(linkToFileName(mechanism))



@app.route("/search", methods = ["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("reactionMapSearch.html")
    else:
        pass

@app.errorhandler(404)
def notFound(temp):
    return render_template("reactionMap404.html")

if __name__ == "__main__":
    app.run()
