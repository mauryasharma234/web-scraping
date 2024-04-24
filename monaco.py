functions = [{'name': 'AND', 'signature': 'AND()', 'description': 'Returns TRUE if all of its arguments are TRUE.Category: Logical', 'parameters': []}, {'name': 'FALSE', 'signature': 'FALSE()', 'description': 'Returns the logical value FALSE.Category: Logical', 'parameters': []}, {'name': 'IF', 'signature': 'IF(logical_test, value_if_true, value_if_false)', 'description': 'Specifies a logical test to perform.Category: Logical', 'parameters': [{'name': 'logical_test', 'type': '*', 'description': ''}, {'name': 'value_if_true', 'type': '*', 'description': ''}, {'name': 'value_if_false', 'type': '*', 'description': ''}]}, {'name': 'IFERROR', 'signature': 'IFERROR(value,value_if_error)', 'description': 'Returns a value you specify if a formula evaluates to an error; otherwise, returns the result of theformula.Category: Logical', 'parameters': [{'name': 'value', 'type': '*', 'description': 'The argument that is checked for an error.'}, {'name': 'value_if_error', 'type': '*', 'description': 'The value to return if the formula evaluates to an error. Thefollowing error types are evaluated: #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or#NULL!.'}]}, {'name': 'IFNA', 'signature': 'IFNA()', 'description': 'Returns the value you specify if the expression resolves to #N/A, otherwise returns the result ofthe expression.Category: Logical', 'parameters': []}, {'name': 'IFS', 'signature': 'IFS()', 'description': 'Checks whether one or more conditions are met and returns a value that corresponds to the first TRUEcondition.Category: Logical', 'parameters': []}, {'name': 'NOT', 'signature': 'NOT()', 'description': 'Reverses the logic of its argument.Category: Logical', 'parameters': []}, {'name': 'OR', 'signature': 'OR()', 'description': 'Returns TRUE if any argument is TRUE.Category: Logical', 'parameters': []}, {'name': 'SWITCH', 'signature': 'SWITCH()', 'description': 'Evaluates an expression against a list of values and returns the result corresponding to the firstmatching value. If there is no match, an optional default value may be returned.Category: Logical', 'parameters': []}, {'name': 'TRUE', 'signature': 'TRUE()', 'description': 'Returns the logical value TRUE.Category: Logical', 'parameters': []}, {'name': 'XOR', 'signature': 'XOR(args)', 'description': 'Returns a logical exclusive OR of all arguments.Category: Logical', 'parameters': [{'name': 'args', 'type': '*', 'description': 'logical1, logical2,… Logical 1 is required, subsequent logicalvalues are optional. 1 to 254 conditions you want to test that can be either TRUE orFALSE, and can be logical values, arrays, or references.'}]}]
answers = []
for function in functions:
    # print(function)
    # print("\n")
    insertText = ""

    insertText += function['name'] + " " + "("
    cnt = 1
    for parameter in function['parameters']:
        if cnt == len(function['parameters']):
            insertText += "${" + str(cnt) + ":" + parameter['name'] + "}"
        else:
            insertText += "${" + str(cnt) + ":" + parameter['name'] + "}, "
        cnt += 1
    insertText += ")"

    ans= {
        "label": function['name'],
        "kind": "monaco.languages.CompletionItemKind.Snippet",
        "insertText": insertText,
        "insertTextRules": "monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet",
        "documentation": function['name'] + " STATEMENT",
        "range": "range"
    }
    
    answers.append(ans)
    

for ans in answers:
    print(ans)  