document.getElementById("infoForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var country = document.getElementById("country").value;
    var userName = document.getElementById("userName").value;
    var password = document.getElementById("password").value;
    let mutual = findMutualString(userName, password);
    displayResult(mutual);
});

function navigateToNewPage() {
    window.location.href = "password_meter.html";
}

function findMutualString(string1, string2) {
    let mutualString = '';
    
    // Convert strings to lowercase for case-insensitive comparison
    const lowerString1 = string1.toLowerCase();
    const lowerString2 = string2.toLowerCase();
    
    // Loop through each character in the first string
    for (let i = 0; i < lowerString1.length; i++) {
      const char = lowerString1.charAt(i);
      
      // Check if the character exists in the second string
      if (lowerString2.includes(char)) {
        // Append the common character to the mutual string
        mutualString += char;
      }
    }
    
    // Check if the mutual string has at least three characters
    if (mutualString.length >= 3) {
      return 1;
    } else {
      return 0;
    }
  }
  function displayResult(mutual) {
    var resultContainer = document.getElementById("resultContainer");
    var feedback_1 = "";
    var feedback_2 = "If you want to improve the strength of your current password click 'Continue'"
    if (mutual == 1){
        feedback_1 = "There appears to be a similarity between your user name and password. Using open data for passwords such as email addresses and user names) can make them easily guessable. Due to this, you should refrain from doing so.\n"
    }
    resultContainer.innerHTML = "<p_1>Detailed Feedback:"+ "<br>"+"</p_1>" + "<p_2>" + feedback_1 + "<br>"+ "<br>" +"</p_2>" + "<p_3>" + feedback_2 +"</p_3>";
    var response = "Continue";
    var responseButton = document.getElementById("responseButton");
    responseButton.style.display = "inline";
    responseButton.innerText = response;
    resultContainer.style.display = "block";
}
