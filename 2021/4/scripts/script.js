


let grid_list = document.getElementById('#input_grid').innerHTML.split(' ').filter(isEmpty)
let input_numbers = document.getElementById('#input_numbers').innerHTML.split(',').filter(isEmpty)
let winning_grids = []
for (let each in input_numbers) {
    input_numbers[each] = input_numbers[each].trim()
}
for (let each in grid_list) {
    grid_list[each] = grid_list[each].trim()
}


function isEmpty(value) {
    return value !== '' & value !== '\n'
}


let grid_array = convertToArray(convertToArray(grid_list))

function convertToArray(list, rows = 5) {
    let itemsPerRow = rows;
    return list.reduce((acc, val, ind) => {
        const currentRow = Math.floor(ind / itemsPerRow);
        if (!acc[currentRow]) {
            acc[currentRow] = [val];
        } else {
            acc[currentRow].push(val);
        }
        return acc;
    }, []);
}

function create_grids() {
    let part_one = document.getElementById('#part_one');
    let tables_one = document.createElement("div");
    tables_one.id = '#tables_one'
    for (let grid in grid_array) {
        let table = document.createElement("table")
        for (let row in grid_array[grid]) {
            let tr = document.createElement("tr")
            for (let cell in grid_array[grid][row]) {
                let td = document.createElement("td")
                let cellText = document.createTextNode(grid_array[grid][row][cell])
                td.appendChild(cellText);
                tr.appendChild(td)
                tr.style.backgroundColor = "rgb(" + Math.random() * 200 + 100 + ", 255, 221, 0.4)"
            }
            table.appendChild(tr)
        }
        table.style.transform = 'rotate(' + (Math.random() * 4 - 2) + 'deg)'
        table.style.margin = '20px'
        tables_one.appendChild(table)
    }
    part_one.appendChild(tables_one)

}

let drawn = 0
function drawNumber() {
    let current_number = input_numbers[drawn]
    if (drawn % 6 === 0) {
        num_string = document.createElement('p')
        num_string.style.transform = 'rotate(' + (Math.random() * 4 - 2) + 'deg)'
        num_string.style.backgroundColor = "rgb(255," + Math.random() * 200 + 100 + ", 150, 0.4)"

    }
    num_string.appendChild(document.createTextNode(input_numbers[drawn] + ' '))
    document.getElementById("#floating").appendChild(num_string)

    check_each_cell(drawn)
    drawn++
}

function check_each_cell(number) {
    for (let grid in grid_array) {
        for (let row in grid_array[grid]) {
            for (let cell in grid_array[grid][row]) {
                if (grid_array[grid][row][cell] === input_numbers[number]) {
                    colorCell(grid, row, cell)
                    checkForWinners(number, grid, row, cell)
                }
            }
        }
    }
}

function colorCell(grid, row, cell) {
    let grids = document.getElementById("#tables_one")
    let tables = grids.getElementsByTagName("table")
    let rows = tables[grid].getElementsByTagName("tr")
    let cells = rows[row].getElementsByTagName('td')
    let td = cells[cell]
    td.style.backgroundColor = "rgb(255, 149, 149)"
}

function checkForWinners(number, grid, row, cell) {

    let colum = [];
    let row_ = grid_array[grid][row]
    for (let each in grid_array[grid]) {
        colum.push(grid_array[grid][each][cell])
    }
    let counter = 0
    for (let each in colum) {
        if (input_numbers.slice(0, number + 1).includes(String(colum[each]))) {
            counter++
        }
    }

    let counter2 = 0
    for (let each in row_) {
        if (input_numbers.slice(0, number + 1).includes(String(row_[each]))) {
            counter2++
        }
    }
    if (counter2 === 5 || counter === 5) {
        if (!winning_grids.includes(grid)) {
            winning_grids.push(grid)

            if (winning_grids.length === grid_array.length) {
                console.log(calculate_result(grid, number))
            }
        }
        printWin(grid, number)
        calculate_result(grid, number)

    }
}

let printWin = (grid, number) => {
    if (typeof (winningP) === 'undefined') {
        winningP = document.createElement('p')
        winningP.appendChild(document.createTextNode("CONRATS!! THE WINNING TICKET IS #" + String(grid)))
        winningP.className = 'floating_2 rotate2'
        let part_one = document.getElementById('#part_one');
        part_one.appendChild(winningP)
        calculate_result(grid, number)
    }

}
let calculate_result = (grid, number) => {
    sum_of_unmarked = 0
    for (let i in grid_array[grid]) {
        for (let j in grid_array[grid][i]) {
            if (!input_numbers.slice(0, number + 1).includes(grid_array[grid][i][j])) {
                sum_of_unmarked += Number(grid_array[grid][i][j])
            }
        }
    }
    return (sum_of_unmarked * input_numbers[number])

}


create_grids()
