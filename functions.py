"""
function definitions
"""

def list_assets(ws):
    """
		function liệt kê tên các tài sản
		param: worksheet 'input'

		return: tên các tài sản
    """

    name = []
    ws1 = ws
    j = 1
    for i in range(1, ws1.max_column + 2):
        cell = ws1.cell(row = 1, column= i)
        if cell.value != None:
            cell.value = cell.value.strip().lower()
            if cell.value != 'open' and cell.value != 'close':
                name.append(cell.value.upper()) 
        elif cell.value == None:
            cell.value = 'Delta' + " " + str(j)
            j+=1

    return name

def calc_delta(ws):
    ws1 = ws
    for i in range(4, ws1.max_column + 4, 4):
        for j in range(2, ws1.max_row + 2, 1):
            cell = ws1.cell(row = j, column= i)
            open = cell.offset(row = 0, column= -2)
            close = cell.offset(row = 0, column= -1)
            if open.value is None or close.value is None:
                break
            else :
                cell.value = (float(close.value) - float(open.value))/float(open.value) # Tính delta 

def calc_stdev(df, name, delta):
    """
        function tính standard deviation của từng tài sản
        @param: 
            df: input worksheet
            name: tên tài sản
            delta: cột delta - daily change của tài sản đó
        return:
            dictionary key: tên tài sản - value: std. dev. tài sản đó
    """

    std = []

    for i in range(len(df.columns)):
        if 'Delta' in df.columns[i]:
            delta.append(df.columns[i]) #Pick ra các cột số delta


    for i in range(0, len(delta)):
        column = df[str(delta[i])]
        stdev = column.std()
        std.append(stdev)

    stdev_dict = dict(zip(name,std))

    return stdev_dict