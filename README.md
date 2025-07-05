# Image-Generator
This is an Image Generator by user input. Does not use OpenAI API directly. Uses the Hugging Face FLUX.1-dev model.

This is my first repo and I'm a beginner, so it might not be efficient but it was my first attempt at something outside of academics.

To use this image generator, you will need to make your own API key with Hugging Faces. https://huggingface.co/settings/tokens. Use this and set the Permissions to **Read. The default permission is FineGrained, so make sure to switch it to **Read before creating your API key. (It asks for your key only at runtime)

Please remember to also run -    pip install requests

in your command terminal

Since I am using a free account and a free API, there is a limit on how many images can be generated, after which it will display the status code of 402 implying that it needs a payment per image to continue. If you have a paid account and pay for images, you will not face such an issue. 

If you reach the limit on free images, the limit resets every hour or so.

Reiterating, this is my first project relating to API's, so please excuse the issues that may follow. 
