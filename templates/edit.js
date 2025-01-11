const add_button = document.getElementById("btn-add");
const name_list = document.getElementById("name-list");
const table_1 = document.getElementById("table_1").getElementsByTagName("tbody")[0];
const table_2 = document.getElementById("table_2").getElementsByTagName("tbody")[0];
const table_2_head = document.getElementById("table_2").getElementsByTagName("thead")[0].getElementsByTagName("tr")[1];
const water_caption = document.getElementById("water-caption");

for (var i = 0; i < name_list.childElementCount; i++) {
    const li = name_list.children[i];
    li.children[0].addEventListener("input", e => rename(e, li.children[0]));
    li.children[1].addEventListener("click", e => del(e, li.children[1]));
}

function del(e, el) {
    const index = Number(el.parentElement.getAttribute("index"));

    const list_line = name_list.getElementsByTagName("li")[index];
    const tb1_line = table_1.getElementsByTagName("tr")[index];
    const tb2_column = table_2.querySelectorAll("td[index='" + index + "']");
    const tb2_head = document.getElementById("column-" + index);

    list_line.remove();
    tb1_line.remove();
    tb2_column.forEach(td => td.remove());
    tb2_head.remove();

    size--;
    water_caption.setAttribute("colspan", size);

    const tb1 = table_1.getElementsByTagName("tr");

    for (var i = index + 1; i <= size; i++) {
        const tb1_line = tb1[i - 1];
        const tb2_column = table_2.querySelectorAll("td[index='" + i + "']");
        const tb2_head = document.getElementById("column-" + i);
        const li = name_list.children[i - 1];

        const new_index = i - 1;

        li.setAttribute("index", new_index);
        li.children[0].name = "name-" + new_index;

        tb2_head.id = "column-" + new_index;

        for (var i = 0; i < {{ chym_size }}; i++) {
            tb2_column[i].setAttribute("index", new_index);
            tb2_column[i].children[0].setAttribute("name", "chym-" + new_index + "-" + i);
        }

        tb1_line.children[0].id = "name-" + new_index;
        for (var i = 1; i < 4; i++) {
            tb1_line.children[i].children[0].setAttribute("name", "base-" + new_index + "-" + i);
        }
    }
}
function rename(e, el) {
    const index = Number(el.parentElement.getAttribute("index"));
    console.log(index);

    const tb1_head = document.getElementById("name-" + index);
    const tb2_head = document.getElementById("column-" + index);

    tb1_head.innerHTML = el.value;
    tb2_head.innerHTML = el.value;
}

add_button.addEventListener("click", e => {
    size++;
    water_caption.setAttribute("colspan", size);

    const li = document.createElement("li");
    li.setAttribute("index", size - 1);

    const li_name = document.createElement("input");
    li_name.type = "text";
    li_name.name = "name-" + (size - 1);
    li_name.addEventListener("input", e => rename(e, li_name));

    li.appendChild(li_name);

    const li_del = document.createElement("input");
    li_del.type = "button";
    li_del.value = "-";
    li_del.addEventListener("click", e => del(e, li_del));

    li.appendChild(li_del);

    name_list.appendChild(li);

    const tb2_header = document.createElement("th");
    tb2_header.id = "column-" + (size - 1);

    table_2_head.appendChild(tb2_header);

    const tb2_trs = table_2.getElementsByTagName("tr");

    for (var i = 0; i < {{ chym_size }}; i++) {
        const td = document.createElement("td");
        td.setAttribute("index", size - 1);

        const input = document.createElement("input");
        input.type = "number";
        input.value = "0";
        input.name = "chym-" + (size - 1) + "-" + i;

        td.appendChild(input);
        tb2_trs[i].appendChild(td);
    }

    const tb1_line = document.createElement("tr");

    const tb1_th = document.createElement("th");
    tb1_th.id = "name-" + (size - 1);
    tb1_line.appendChild(tb1_th);

    for (var i = 1; i < 4; i++) {
        const td = document.createElement("td");
        const input = document.createElement("input");
        input.type = "number";
        input.value = "0";
        input.name = "base-" + (size - 1) + "-" + i;

        td.appendChild(input);
        tb1_line.appendChild(td);
    }

    table_1.appendChild(tb1_line);
});