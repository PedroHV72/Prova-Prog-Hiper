document.getElementById('mensagem_curtida').onclick = function() {
    Swal.fire({
        title: 'Vídeo curtido!',
        icon: 'success',
        confirmButtonText: 'Sair'
      })
    }

document.getElementById('mensagem_comentario').onclick = function() {
    Swal.fire({
        title: 'Comentário enviado!',
        icon: 'success',
        confirmButtonText: 'Sair'
        })
    }