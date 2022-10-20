import json
import re
from pydoc import describe

jsonPath = "../../characters.json"


def processJson():
    # read json file
    with open(jsonPath, "r") as jsonFile:
        data = json.load(jsonFile)

    for character in data:
        # remove references
        removeReferences(character)
        removeExcessiveInformation(character)
        replaceUtf8toAscii(character)
        removeOtherCharacters(character)
        
    return data
    
def removeReferences(character):
    
    description = character["description"]
    regex = r"\[\d+\]"

    descriptionWithoutReferences = re.sub(regex, "", description)
    character["description"] = descriptionWithoutReferences

def removeExcessiveInformation(character):
    description = character["description"]
    
    if description.count("\n") > 1:
        description = description.split("\n")
        description = description[-2]
        character["description"] = description
    else:
        character["description"] = description.replace("\n", "")
        
        
def replaceUtf8toAscii(character):
    description = character["description"]
    name = character["name"]
    character["description"] = description.encode("ascii", "ignore").decode("utf-8")
    character["name"] = name.encode("ascii", "ignore").decode("utf-8")
    
def removeOtherCharacters(character):
    description = character["description"]
    description = description.replace("\"", "")
    character["description"] = description
    
if __name__ == "__main__":
    processedJson = processJson()
    jsonNameRegex = r"\/(\w+)\.json"
    jsonName = re.search(jsonNameRegex, jsonPath).group(1)
    jsonNewPath =  "../../processed_json/" + jsonName + "_processed.json"
    
    print(jsonName)
    
    with open(jsonNewPath, "w") as jsonFile:
        json.dump(processedJson, jsonFile, indent=4)
