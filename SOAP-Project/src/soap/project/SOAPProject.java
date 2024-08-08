/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package soap.project;

import javax.xml.ws.Endpoint;

/**
 *
 * @author 20171014040001
 */
public class SOAPProject {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       Endpoint.publish(
            "http://10.25.2.65:9877/geraSenha", 
            new ServidorSOAP()
        );
        System.out.println("Servico em execucao...");
    }
    
}
