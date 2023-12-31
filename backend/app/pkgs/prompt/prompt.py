from app.pkgs.prompt.subtask_pro import SubtaskPro
from app.pkgs.prompt.requirement_basic import RequirementBasic
from app.pkgs.prompt.requirement_pro import RequirementPro
from app.pkgs.prompt.api_pro import ApiPro
from app.pkgs.prompt.api_basic import ApiBasic
from app.pkgs.prompt.subtask_basic import SubtaskBasic
from app.pkgs.prompt.subtask_java_pro import SubtaskJavaPro
from app.pkgs.prompt.subtask_vue_pro import SubtaskVuePro
from app.pkgs.prompt.code_basic import CodeBasic
from app.pkgs.prompt.code_pro import CodePro
from config import GRADE

def clarifyRequirement(user_prompt, global_context):
    if GRADE == "base":
        obj = RequirementBasic()
    else:
        obj = RequirementPro()
        
    return obj.clarifyRequirement(user_prompt, global_context)

def clarifyAPI(user_prompt, global_context):
    if GRADE == "base":
        obj = ApiBasic()
    else:
        obj = ApiPro()
        
    return obj.clarifyAPI(user_prompt, global_context)

def splitTask(feature, serviceName, apiDocUrl):
    if GRADE == "base":
        obj = SubtaskBasic()
    else:
        if "java" in serviceName:
            obj = SubtaskJavaPro()
        if "vue" in serviceName:
            obj = SubtaskVuePro()
        else:
            obj = SubtaskPro()

    return obj.splitTask(feature, serviceName, apiDocUrl)

def aiReferenceRepair(newCode, referenceCode, fileTask):
    if GRADE == "base":
        obj = CodeBasic()
    else:
        obj = CodePro()
        
    return obj.aiReferenceRepair(newCode, referenceCode, fileTask)

def aiAnalyzeError(message):
    if GRADE == "base":
        obj = CodeBasic()
    else:
        obj = CodePro()
        
    return obj.aiAnalyzeError(message)

def aiFixError(solution, code):
    if GRADE == "base":
        obj = CodeBasic()
    else:
        obj = CodePro()
        
    return obj.aiFixError(solution, code)

def aiCheckCode(fileTask, code):
    if GRADE == "base":
        obj = CodeBasic()
    else:
        obj = CodePro()
        
    return obj.aiCheckCode(fileTask, code)

def aiMergeCode(fileTask, appName, baseCode, newCode):
    if GRADE == "base":
        obj = CodeBasic()
    else:
        obj = CodePro()
        
    return obj.aiMergeCode(fileTask, appName, baseCode, newCode)

def aiGenCode(fileTask, newTask, appName, newCode):
    if GRADE == "base":
        obj = CodeBasic()
    else:
        obj = CodePro()
        
    return obj.aiGenCode(fileTask, newTask, appName, newCode)