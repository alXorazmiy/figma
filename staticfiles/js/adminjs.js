 function myButton() {

                    setTimeout(() =>
                        {
                            var popup1 = document.querySelector('.admin_section1');
                            var popup2 = document.querySelector('.admin_section2');
                            var popup3 = document.querySelector('.admin_section3');
                            popup1.style.display = 'block';
                            popup2.style.display = 'none';
                            popup3.style.display = 'none';
                            document.getElementById('btn1').style.color = 'white';
                    document.getElementById('btn1').style.background = '#3366fe';
                    document.getElementById('btn1').style.opacity = '1';
                    document.getElementById('btn2').style.color = '#3366fe';
                    document.getElementById('btn2').style.background = 'white';
                    document.getElementById('btn2').style.opacity = '0.6';
                    document.getElementById('btn3').style.color = '#3366fe';
                    document.getElementById('btn3').style.background = 'white';
                    document.getElementById('admin_section1').style.display = 'block';
                        }, 200
                    )
}
function myButton2() {
                            var popup1 = document.querySelector('.admin_section1');
                            var popup2 = document.querySelector('.admin_section2');
                            var popup3 = document.querySelector('.admin_section3');
                            popup1.style.display = 'none';
                            popup2.style.display = 'block';
                            popup3.style.display = 'none';
                    document.getElementById('btn2').style.color = 'white';
                    document.getElementById('btn2').style.background = '#3366fe';
                    document.getElementById('btn2').style.opacity = '1';
                    document.getElementById('btn1').style.color = '#3366fe';
                    document.getElementById('btn1').style.background = 'white';
                    document.getElementById('btn1').style.opacity = '0.6';

                    document.getElementById('btn3').style.color = '#3366fe';
                    document.getElementById('btn3').style.background = 'white';
                    document.getElementById('btn3').style.opacity = '0.6';
                    document.getElementById('admin_section1').style.display = 'none';

}
function myButton3() {
                            var popup1 = document.querySelector('.admin_section1');
                            var popup2 = document.querySelector('.admin_section2');
                            var popup3 = document.querySelector('.admin_section3');
                            popup1.style.display = 'none';
                            popup2.style.display = 'none';
                            popup3.style.display = 'block';
                    document.getElementById('btn3').style.color = 'white';
                    document.getElementById('btn3').style.background = '#3366fe';
                    document.getElementById('btn3').style.opacity = '1';
                    document.getElementById('btn1').style.color = '#3366fe';
                    document.getElementById('btn1').style.background = 'white';
                    document.getElementById('btn1').style.opacity = '0.6';

                    document.getElementById('btn2').style.color = '#3366fe';
                    document.getElementById('btn2').style.background = 'white';
                    document.getElementById('btn2').style.opacity = '0.6';
                    document.getElementById('admin_section3').style.display = 'block';
}
