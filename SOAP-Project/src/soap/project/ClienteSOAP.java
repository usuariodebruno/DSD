/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package soap.project;

import java.net.MalformedURLException;
import java.net.URL;
import javax.xml.namespace.QName;
import javax.xml.ws.Service;

/**
 *
 * @author 20171014040001
 */
public class ClienteSOAP {
    public static void main(String args[]){
        
        try{
            URL url = new URL("http://10.25.2.65:9877/geraSenha?wsdl");
            QName qname = new QName("http://soap/", "ServidorSOAPService");
            
            Service ws = Service.create(url, qname);
            SOAPInterface calc = ws.getPort(SOAPInterface.class);            
            
            String nome = "Bruno";
            System.out.println("Resposta: " + calc.olaMundo(nome));
            System.out.println("Senha: " + calc.gerarSenha(8, false, false));
            System.out.println("Senha forte: " + calc.gerarSenha(12, true, true));
            
        }catch(MalformedURLException mue){
            mue.printStackTrace();
        }
    }
}
