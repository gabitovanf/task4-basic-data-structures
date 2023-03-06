import pandas as pd
from pprint import pprint

def writeValueToDataFrame(line: str, dfdict):
    arrayType, sheetName, colValuePair = tuple(map(lambda s: s.strip(), line.split(':')))
    col, value = tuple(map(lambda s: s.strip(), colValuePair.split('->')))

    print(arrayType, sheetName, colValuePair, col, value)

    df = dfdict.setdefault(sheetName, pd.DataFrame())

    index = df.index
    columns = df.columns

    if not arrayType in index:
        index = index.insert(index.size, arrayType)

    if not col in columns:
        columns = columns.insert(columns.size, col)

    # print('index', index, type(index), index.array, bool(arrayType in index))
    # print('columns', columns, type(columns), columns.array)

    df = pd.DataFrame(df, index=index, columns=columns)

    df.at[arrayType, col] = value

    dfdict[sheetName] = df



def readReport(path: str, dfdict: dict):
    with open(path, 'r') as f:

        lines = f.readlines()

        for s in lines:
            s = s.strip()
            if len(s) < 1:
                continue
            writeValueToDataFrame(s, dfdict)

    return dfdict


def writeDataFramesToXlsx(dfdict:dict, path: str):
    with pd.ExcelWriter(path) as writer:
        for name, df in dfdict.items():
            print(name, len(name))
            df.to_excel(writer, name)


dataFrameDict = readReport('reports/ResultsSingleArray.txt', {})
dataFrameDict = readReport('reports/ResultsVectorArray.txt', dataFrameDict)
dataFrameDict = readReport('reports/ResultsFactorArray.txt', dataFrameDict)
dataFrameDict = readReport('reports/ResultsMatrixArray.txt', dataFrameDict)
dataFrameDict = readReport('reports/ResultsListArrayAdapter.txt', dataFrameDict)

writeDataFramesToXlsx(dataFrameDict, 'report-sheets.xlsx')

