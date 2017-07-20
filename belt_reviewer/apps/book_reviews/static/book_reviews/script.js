function star_string(rating){
    var yellow = rating;
    var white = 5 - rating;
    var html_string = "Rating : ";
    for (var i = 1; i <= yellow; i+=1){
        html_string += "<img class='star-pic' src='/static/book_reviews/yellow_star.png'> ";
    }
    for (var i = 1; i <= white; i+=1){
        html_string += "<img class='star-pic' src='/static/book_reviews/white_star.jpg'> ";
    }
    return html_string;
}

$(document).ready(function() {
    $('.star-images').each(function(i) {
        var stars = ($(this).html());
        $(this).html(star_string(stars));
    });       
});