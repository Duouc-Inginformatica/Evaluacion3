document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario").addEventListener('submit', validarFormulario); 
  });

  function validarFormulario(evento) {
    evento.preventDefault();
    var rut = document.getElementById('txt_rut').value;
    console.log('se detecto un evento en l rut');
    if(rut.length == 0) {
      alert('No has escrito nada en el rut');
      return;
    }
    var nombre = document.getElementById('txt_nombre').value;
    if (nombre.length == 0) {
      alert('El nombre no puede estar vacio');
      return;
    }
    
    var txt_appaterno = document.getElementById('txt_appaterno').value;
    if (txt_appaterno.length == 0) {
        alert('El apellido paterno no puede estar vacio');
        return;
        }
    var txt_apmaterno = document.getElementById('txt_apmaterno').value;
    if (txt_apmaterno.length == 0) {
        alert('El apellido materno no puede estar vacio');
        return;
      }
    var edad = document.getElementById('txt_edad').value;
    if (edad.length == 0) {
        alert('La edad no puede estar vacia');
        return;
        }
    var vacuna = document.getElementById('txt_vacuna').value;
    if (vacuna.length == 0) {
        alert('La vacuna no puede estar vacia');
        return;
        }
    var txt_fecha = document.getElementById('txt_fecha').value;
    if (txt_fecha.length == 0) {
         alert('La fecha no puede estar vacia');
         return;
         }
        
    this.submit();
        
}
