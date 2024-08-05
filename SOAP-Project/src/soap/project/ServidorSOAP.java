/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package soap.project;

import javax.jws.WebService;

/**
 *
 * @author 20171014040001
 */
@WebService(endpointInterface = "soap.project.SOAPInterface")
public class ServidorSOAP implements SOAPInterface{

    @Override
    public String olaMundo(String nome) {
        System.out.println("OLÁ MUNDO ACESSADA..");
        return "OLÁ MUNDO: " + nome;    
    }
    
}
