/*INSERE DADOS NA TABELA DE PERFIL*/
INSERT INTO LABDATABASE.PERFILS VALUES(PERFILS_CODIGO_SEQ.NEXTVAL, 'ATLETA DE FIM DE SEMANA', 1.25);
INSERT INTO LABDATABASE.PERFILS VALUES(PERFILS_CODIGO_SEQ.NEXTVAL, 'ATLETA DE ALTA PERFORMANCE', 2.5);
INSERT INTO LABDATABASE.PERFILS VALUES(PERFILS_CODIGO_SEQ.NEXTVAL, 'ATLETA PROFISSIONAL', 2.0);
INSERT INTO LABDATABASE.PERFILS VALUES(PERFILS_CODIGO_SEQ.NEXTVAL, 'CICLISTA', 1.3);
INSERT INTO LABDATABASE.PERFILS VALUES(PERFILS_CODIGO_SEQ.NEXTVAL, 'AMANTE DE CAMINHADA', 1.1);

/*INSERE DADOS NA TABELA DE USUARIO*/
INSERT INTO LABDATABASE.USUARIO VALUES(USUARIO_CODIGO_SEQ.NEXTVAL, 'TESTE','TESTE@gmail.com',25,1.92,95,5);
INSERT INTO LABDATABASE.USUARIO VALUES(USUARIO_CODIGO_SEQ.NEXTVAL, 'JOÃO','JOÃO@gmail.com', 30, 1.75, 70, 2);
INSERT INTO LABDATABASE.USUARIO VALUES(USUARIO_CODIGO_SEQ.NEXTVAL, 'MARIA','MARIA@gmail.com', 28, 1.68, 60, 1);
INSERT INTO LABDATABASE.USUARIO VALUES(USUARIO_CODIGO_SEQ.NEXTVAL, 'ANA','ANA@gmail.com', 32, 1.62, 58, 3);
INSERT INTO LABDATABASE.USUARIO VALUES(USUARIO_CODIGO_SEQ.NEXTVAL, 'CARLOS','CARLOS@gmail.com', 45, 1.78, 85, 4);
INSERT INTO LABDATABASE.USUARIO VALUES(USUARIO_CODIGO_SEQ.NEXTVAL, 'MARIA','MARIA@gmail.com',25,1.92,95,5);
INSERT INTO LABDATABASE.USUARIO VALUES(USUARIO_CODIGO_SEQ.NEXTVAL, 'BRUNO','BRUNO@gmail.com', 30, 1.75, 70, 3);
INSERT INTO LABDATABASE.USUARIO VALUES(USUARIO_CODIGO_SEQ.NEXTVAL, 'JULIA','JU@gmail.com', 28, 1.68, 60, 5);
INSERT INTO LABDATABASE.USUARIO VALUES(USUARIO_CODIGO_SEQ.NEXTVAL, 'BIANCA','BI@gmail.com', 32, 1.62, 58, 3);
INSERT INTO LABDATABASE.USUARIO VALUES(USUARIO_CODIGO_SEQ.NEXTVAL, 'FABIO','FABIO@gmail.com', 45, 1.78, 85, 4);

/*INSERE DADOS NA TABELA DE AGENDA*/
INSERT INTO LABDATABASE.AGENDA VALUES(AGENDA_CODIGO_SEQ.NEXTVAL, 4, 2, 9,SYSDATE, 1);
INSERT INTO LABDATABASE.AGENDA VALUES(AGENDA_CODIGO_SEQ.NEXTVAL, 3, 1, 8,SYSDATE,5);
INSERT INTO LABDATABASE.AGENDA VALUES(AGENDA_CODIGO_SEQ.NEXTVAL, 4, 2, 9, SYSDATE, 4);
INSERT INTO LABDATABASE.AGENDA VALUES(AGENDA_CODIGO_SEQ.NEXTVAL, 1, 3, 10, SYSDATE, 2);
INSERT INTO LABDATABASE.AGENDA VALUES(AGENDA_CODIGO_SEQ.NEXTVAL, 2, 4, 11, SYSDATE, 3);
INSERT INTO LABDATABASE.AGENDA VALUES(AGENDA_CODIGO_SEQ.NEXTVAL, 1, 5, 14, SYSDATE, 4);








COMMIT;