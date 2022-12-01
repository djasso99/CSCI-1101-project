window.addEventListener("load", function ()
{
    // Get click elements.
    let clickbuttonelement = document.getElementById("click_button");
    let clickcounterelement = document.getElementById("click_counter");

    // Counter value
    let counter = 0;

    // Button click function
    let clickbuttonfunction = function ()
    {
        //incrment counter
        counter++;

        //Update click counter text
        clickcounterelement.innerHTML = counter;
    };

    // attach click function to button
    clickbuttonelement.addEventListener("click", clickbuttonfunction); 
});