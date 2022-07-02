from pyodide import create_proxy
from js import console

x_replace = Element("x_replace").element
x_reverse = Element("x_reverse").element
x_case = Element("x_case_transform").element
x_numeral = Element("x_numeral_system").element
x_caesar = Element("x_caesar").element
x_vigenere = Element("x_vigenere").element
x_alphabetical = Element("x_alphabetical").element
x_rail_fence = Element("x_rail_fence").element
x_base32 = Element("x_base32").element
x_base64 = Element("x_base64").element
x_ascii85 = Element("x_ascii85").element
x_unicode = Element("x_unicode").element
x_url_encode = Element("x_url_encode").element
x_hash_func = Element("x_hash_func").element
x_hmac = Element("x_hmac").element

goto_feature = Element("goto_feature").element

breadcrumb1 = Element("breadcrumb1").element
breadcrumb2 = Element("breadcrumb2").element

view_feature = Element("view_feature").element
view_main = Element("view_main").element

view_x_caesar = Element("view_x_caesar").element

is_encode = Element("is_encode").element
tab_encode = Element("tab_encode").element
tab_decode = Element("tab_decode").element

input = Element("input").element
output = Element("output").element

x_caesar_shift = Element("x_caesar_shift").element
x_caesar_shift_plus = Element("x_caesar_shift_plus").element
x_caesar_shift_minus = Element("x_caesar_shift_minus").element
# x_caesar_case = Element("x_caesar_case").element
x_caesar_process = Element("x_caesar_process").element


def show_feature():
    view_main.classList.add("is-hidden")
    view_feature.classList.remove("is-hidden")

    view_x_caesar.classList.add("is-hidden")


def show_main(id):
    view_main.classList.remove("is-hidden")
    view_feature.classList.add("is-hidden")
    breadcrumb1.innerHTML = id.closest(":not(button)").previousElementSibling.innerHTML
    breadcrumb2.innerHTML = id.innerHTML


def switch_input():
    temp = input.value
    input.value = output.value
    output.value = temp


def tab_encode_click(event):
    if not tab_encode.classList.contains("is-active"):
        tab_encode.classList.add("is-active")
        tab_decode.classList.remove("is-active")
        is_encode.value = 1
        switch_input()


def tab_decode_click(event):
    if not tab_decode.classList.contains("is-active"):
        tab_encode.classList.remove("is-active")
        tab_decode.classList.add("is-active")
        is_encode.value = 0
        switch_input()


def goto_feature_click(event):
    show_feature()


def x_replace_click(event):
    show_main(x_replace)


def x_reverse_click(event):
    show_main(x_reverse)


def x_case_click(event):
    show_main(x_case)


def x_numeral_click(event):
    show_main(x_numeral)


def x_caesar_click(event):
    show_main(x_caesar)
    view_x_caesar.classList.remove("is-hidden")


def x_vigenere_click(event):
    show_main(x_vigenere)


def x_alphabetical_click(event):
    show_main(x_alphabetical)


def x_rail_fence_click(event):
    show_main(x_rail_fence)


def x_base32_click(event):
    show_main(x_base32)


def x_base64_click(event):
    show_main(x_base64)


def x_ascii85_click(event):
    show_main(x_ascii85)


def x_unicode_click(event):
    show_main(x_unicode)


def x_url_encode_click(event):
    show_main(x_url_encode)


def x_hash_func_click(event):
    show_main(x_hash_func)


def x_hmac_click(event):
    show_main(x_hmac)


def x_caesar_shift_plus_click(event):
    x_caesar_shift.value = int(x_caesar_shift.value) + 1


def x_caesar_shift_minus_click(event):
    x_caesar_shift.value = int(x_caesar_shift.value) - 1


def x_caesar_encode_decode(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += char

    return result


def x_caesar_process_click(event):
    if int(is_encode.value) == 1:
        output.value = x_caesar_encode_decode(input.value, int(x_caesar_shift.value))
    else:
        output.value = x_caesar_encode_decode(input.value, -int(x_caesar_shift.value))


def main():
    goto_feature.addEventListener("click", create_proxy(goto_feature_click))

    tab_encode.addEventListener("click", create_proxy(tab_encode_click))
    tab_decode.addEventListener("click", create_proxy(tab_decode_click))

    x_replace.addEventListener("click", create_proxy(x_replace_click))
    x_reverse.addEventListener("click", create_proxy(x_reverse_click))
    x_case.addEventListener("click", create_proxy(x_case_click))
    x_numeral.addEventListener("click", create_proxy(x_numeral_click))
    x_caesar.addEventListener("click", create_proxy(x_caesar_click))
    x_vigenere.addEventListener("click", create_proxy(x_vigenere_click))
    x_alphabetical.addEventListener("click", create_proxy(x_alphabetical_click))
    x_rail_fence.addEventListener("click", create_proxy(x_rail_fence_click))
    x_base32.addEventListener("click", create_proxy(x_base32_click))
    x_base64.addEventListener("click", create_proxy(x_base64_click))
    x_ascii85.addEventListener("click", create_proxy(x_ascii85_click))
    x_unicode.addEventListener("click", create_proxy(x_unicode_click))
    x_url_encode.addEventListener("click", create_proxy(x_url_encode_click))
    x_hash_func.addEventListener("click", create_proxy(x_hash_func_click))
    x_hmac.addEventListener("click", create_proxy(x_hmac_click))

    x_caesar_shift_plus.addEventListener(
        "click", create_proxy(x_caesar_shift_plus_click)
    )
    x_caesar_shift_minus.addEventListener(
        "click", create_proxy(x_caesar_shift_minus_click)
    )
    x_caesar_process.addEventListener("click", create_proxy(x_caesar_process_click))


main()
