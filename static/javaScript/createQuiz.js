$(document).ready(function(){
    // Keep track of the number of questions and options for the questions
    let optionCount = 1;
    let questionCount = 1; 

    $('#addOptionButtonId').click(function(){
        //Adding one to option count every time the button is clicked
        optionCount++

        //putting the html code into a variable to be added to the page
        let newOption = "<li><input class='answerBoxInput' type='text' placeholder='Answer input' name='answer${optionCount}Input'><input type='checkbox' name='correctAnswer${optionCount}'></li>";

        //Adding the new option to the answers section
        $('#answerInput').append(newOption);
    })

    $('#addQuestionButtonId').click(function(){
        questionCount++;

        // clone the section that contains the quiz
        let newQuestion = $('#addQuestionId').clone();

        // Get rid of any inputs that are currently there
        newQuestion.find('input[type="text"]').val('');
        newQuestion.find('input[type="checkbox"]').prop('checked', false);

        // Changing the names of the inputs so that they're unique compared to the other questions
        newQuestion.find('.questionTitle').attr('name', `questionTitleInput${questionCount}`);
        newQuestion.find('ul#answerInput li').each(function(index, element){
            $(element).find('.answerBoxInput').attr('name', `answer${index + 1}Input_${questionCount}`);
            $(element).find('input[type="checkbox"]').attr('name', `correctAnswer${index + 1}_${questionCount}`);
        });

        // Adding the new question to the questions section
        $('#questionsId').append(newQuestion);
    });
})

