$(document).ready(function() {

    $('.farm').hover(
        function() {
            $(this).html("<div class='over'><h2>Farm</h2><p>Earns 10-20 Golds</p><input type='hidden' name='place' value='farm' form='pick_place'><input type='submit' value='Find Gold' id='submit' form='pick_place'></div>")
        },
        function() {
            $(this).html("")
        });
    
    $('.cave').hover(
        function() {
            $(this).html("<div class='over'><h2>Cave</h2><p>Earns 5-10 Golds</p><input type='hidden' name='place' value='cave' form='pick_place'><input type='submit' value='Find Gold' id='submit' form='pick_place'></div>")
        },
        function() {
            $(this).html("")
        });

    $('.house').hover(
        function() {
            $(this).html("<div class='over'><h2>House</h2><p>Earns 2-5 Golds</p><input type='hidden' name='place' value='house' form='pick_place'><input type='submit' value='Find Gold' id='submit' form='pick_place'></div>")
        },
        function() {
            $(this).html("")
        });

    $('.casino').hover(
        function() {
            $(this).html("<div class='over'><h2>Casino</h2><p>Earns/Takes 0-50 Golds</p><input type='hidden' name='place' value='casino' form='pick_place'><input type='submit' value='Risk it!' id='submit' form='pick_place'></div>")
        },
        function() {
            $(this).html("")
        });

});