$(document).on('ready',function() {
    $.ajax( {
        type:"GET",
        contentType:"application/json; charset=utf-8",
        dataType:"json",
        url:"/webService/invitaciones/",
        success:function(data){

            $('#Mensajes').append("<h4>"+"Invitaciones"+"</h4>");
            for (var x=0;x<=(data.i.length - 1);x++){
                for (var y=0;y<=(data.e.length - 1);y++){


                    if (data.i[x].fields.evento == data.e[y].pk) {
                        for (var z=0;z<=(data.u.length - 1);z++){
                            if (data.e[y].fields.creador == data.u[z].pk) {
                                var u_creador =data.u[z].fields.username
                            };

                        } 



                        $('#Mensajes').append(
                            '<li class="message-preview">'+
                            '<div class="media">'+
                            '<span class="pull-left">'+
                            '<img class="media-object" src="http://placehold.it/50x50" alt="">'+
                            '</span>'+
                            '<div class="media-body">'+
                            '<h5 class="media-heading"> <strong>'+ u_creador+


                            '</strong> te ha invitado a un nuevo evento: <em>'+data.e[y].fields.titulo+'</em>'+
                            '</h5>'+
                            '<p class="small text-muted"><i class="fa fa-clock-o"></i> Yesterday at 4:32 PM</p>'+
                            '<p>'+data.e[y].fields.descripcion+'</p>'+
                            '<p><a href="/evento/detail/'+data.e[y].pk+'">Ver invitacion...</a></p>'+
                            '</div>'+
                            '</div>'+
                            '</li>'

                            );
};
}

}
}
});
});










$(document).on('ready',function() {
    $.ajax( {
        type:"GET",
        contentType:"application/json; charset=utf-8",
        dataType:"json",
        url:"/webService/eventos/",
        success:function(data){

            $('#Alertas').append("<h4>"+"Eventos"+"</h4>");
            for (var x=0;x<=(data.i.length - 1);x++){
                for (var y=0;y<=(data.e.length - 1);y++){


                    if (data.i[x].fields.evento == data.e[y].pk) {



                        $('#Alertas').append(
                            '<li><a href="/evento/detail/'+data.e[y].pk+'"> <span class="label label-info">Ver evento</span> '+data.e[x].fields.titulo+'</a></li>'

                            );
                    }
                }
            }
        }
    });
});



