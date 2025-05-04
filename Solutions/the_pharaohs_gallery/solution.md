# The Pharaoh's Gallery
Look at this magnificent scroll. It must be preserved at all cost.
Let's bring it back to our exhibit.

Challenge type: File Upload

## Solution
The web page prompts you to either upload an image or to view the gallery:
![alt text](image.png)

Going to the upload page, you are prompted to upload an image in the following formats: .jpg, .jpeg, .png, .gif.
![alt text](image-1.png)

After uploading an image, it can be seen in the gallery:
![alt text](image-2.png)

After testing different techniques, and uploading different files, the application makes sure that uploaded files has one of the allowed extensions and that the it has the correct "magic bytes".

To get command execution on the system, the "magic bytes" and the IHDR section from a .png file was extracted using the `dd` command. 
![alt text](image-3.png)

The end of the same .png was also extracted using `dd`:
![alt text](image-4.png)

The middle of the file is going to contain the PHP code we want to execute. For this challenge, PHP code was that executes strings passed in the **cmd** paramter:
![alt text](image-5.png)

A single "image" file was created using the cat command:
![alt text](image-6.png)

![alt text](image-7.png)

Uploading the file to the server and accessing it, shows that it want us to supply a command via the **cmd** paramter. Supplying a command results in successfull execution of the command:
![alt text](image-8.png)

After spending some time looking though different files and directories, the flag was located in `/var/www/html/app.py`. Flag: **O24{Th3_Phar40h_Kn0ws_Y0ur_P0lygl0t_Tr1cks}**
![alt text](image-9.png)
