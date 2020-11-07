$(document).ready(function() {

        $('#language-list a').on('click', function(event) {
            event.preventDefault();
            var target = $(event.target);
            var url = target.attr('href');
            var language_code = target.data('language-code');
            var nextpage = target.data('next');
            try {
            $.ajax({
                type: 'POST',
                url: url,
                data: {language: language_code},
                headers: {"X-CSRFToken": getCookie('csrftoken')}
            }).done(function(data, textStatus, jqXHR) {
                try {
                setCookie("django_language",language_code, (10000 * 365 * 24 * 60 * 60));
                alert("success");
                }
                catch(e) {alert("failed cookie");}
                window.location.href = nextpage;
            });
            }
            catch(e) {}
            finally {
                // alert("failed everything")
                // window.location.href = '/' + language_code + nextpage;
            }
        });
        
        function setCookie(cname, cvalue, exp) {
          var d = new Date();
          d.setTime(d.getTime() + (exp));
          var expires = "expires="+ d.toUTCString();
          document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
        }
        
        function getCookie(name) {
            var value = '; ' + document.cookie,
                parts = value.split('; ' + name + '=');
            if (parts.length == 2) return parts.pop().split(';').shift();
        }
    });
