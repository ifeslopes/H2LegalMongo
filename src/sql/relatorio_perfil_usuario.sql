select p.descricao_perfil nome_perfil ,COUNT(*)
  from PERFILS p JOIN USUARIO u on(p.codigo_perfil =u.codigo_perfil) GROUP BY p.descricao_perfil