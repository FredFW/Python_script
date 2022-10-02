# Python_script
Some python scripts to make my life easier


- **generate_text_file**

    - Usage: python generate_text_file.py [input_text] [repeat_times]
    - Use $'   ' To escape sequence:
  
        > python generate_text_file.py $'ABC\n123' 1 \
        > \
        > Output: \
        > ABC \
        > 123 
      
        - **\a** - alert (bell) 
        - **\b** - backspace 
        - **\e** or **\E** - an escape character (not ANSI C) 
        - **\f** - form feed 
        - **\n** - newline 
        - **\r** - carriage return 
        - **\t** - horizontal tab 
        - **\v** - vertical tab 
        - **\\** - backslash 
        - **\'** - single quote 
        - **\"** - double quote 
        - **\?** - question mark 
        - **\nnn** - the eight-bit character whose value is the octal value nnn (one to three octal digits) 
        - **\xHH** - the eight-bit character whose value is the hexadecimal value HH (one or two hex digits) 
        - **\uHHHH** - the Unicode (ISO/IEC 10646) character whose value is the hexadecimal value HHHH (one to four hex digits) 
        - **\UHHHHHHHH** - the Unicode (ISO/IEC 10646) character whose value is the hexadecimal value HHHHHHHH (one to eight hex digits) 
        - **\cx** - a control-x character 


- **insert_text_file.py**

    - Usage: python insert_text_file.py [file_name] [input_text]


- **join_text_file.py**
    
    - python join_text_file.py [mode] [file_name_1] [input_delimiter_text] [file_name_2]
    - Mode: pair / all


- **Simple_HTTP_Server_with_Upload.py**

    - Forked from [UniIsland/SimpleHTTPServerWithUpload.py](https://gist.github.com/UniIsland/3346170)


* **http_server_with_put_method.py**

  1. Save this code in a file and name the file server.py and run it on receiving host.

        > python server.py 80
    

  2. Upload the file to HTTP server using curl on sending host.
    
        > curl 192.77.184.2 --upload-file file.zip
    
