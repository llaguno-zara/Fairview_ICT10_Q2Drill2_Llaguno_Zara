from pyscript import display, document

def add_brand(e):
    document.getElementById('outpu1').innerHTML = ""

    brands = {'Zara Llaguno','Cheree Mendoza','Therese Reyes','Ysabel Valerio', 'Jilliane Tech'}

    input_brand = document.getElementById('input1').value
    input_brand2 = document.getElementById('input2').value

    new_brand_set = {input_brand + "" + input_brand2}

    all_brands = brands | new_brand_set

    total_brands = len(brands | new_brand_set)

    brand_list = "<br>".join(sorted(all_brands))

    document.getElementById('output1').innerHTML = f'All brands: <br> {brand_list}'
    display(f'Total brands: {total_brands}, target="output2"')