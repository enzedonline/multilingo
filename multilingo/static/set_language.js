$(document).ready(function() {

        $('#languagelist a').on('click', function(event) {
            event.preventDefault();
            let target = $(event.currentTarget);
            let nextpage = target.data('nextpage');
            let url = target.attr('href');
            let language_code = target.data('languagecode');
            try {
                $.ajax({
                    type: 'POST',
                    url: url,
                    data: {language: language_code, next: nextpage},
                    headers: {"X-CSRFToken": getCookie('csrftoken')}
                    }).done(function(data, textStatus, jqXHR) {
                        try {
                            setCookie("django_language", language_code, (10000 * 365 * 24 * 60 * 60));
                            }
                        catch(e) {
                            }
                        window.location.href = nextpage;
                        });
                }
            catch(e) {}
            finally {}
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
