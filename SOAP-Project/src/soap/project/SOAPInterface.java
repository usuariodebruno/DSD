/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package soap.project;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.soap.SOAPBinding;

/**
 *
 * @author 20171014040001
 */
@WebService
@SOAPBinding(style=SOAPBinding.Style.RPC)
public interface SOAPInterface {
    @WebMethod String olaMundo(String nome);
    @WebMethod String gerarSenha(int comprimento, boolean incluirNumeros, boolean incluirCaracteresEspeciais);

}
