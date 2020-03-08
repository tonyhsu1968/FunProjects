function run(type, next){

  next = next || 0
    window.SpeechRecognition = window.webkitSpeechRecognition || window.SpeechRecognition;
    let finalTranscript = '';
    let recognition = new window.SpeechRecognition();

    recognition.interimResults = true;
    recognition.maxAlternatives = 10;
    recognition.continuous = true;

    recognition.onresult = (event) => {
      let interimTranscript = '';
      for (let i = event.resultIndex, len = event.results.length; i < len; i++) {
        let transcript = event.results[i][0].transcript;
        if (event.results[i].isFinal) {
          finalTranscript += transcript;
        } else {
          interimTranscript += transcript;
        }
      }

      pattern = /name (.*?) name/
          
      var result = finalTranscript.match(pattern);
      
      // console.log(result) It can be used for debugging JavaScript

      try
      { 
      result = result[1].split(' ').join('');
      finalTranscript= finalTranscript.replace(pattern, result)
      }
      catch(err)
      {

      }
      document.getElementById(type).value = finalTranscript + interimTranscript;
      
      
    }
    recognition.start();
   
}