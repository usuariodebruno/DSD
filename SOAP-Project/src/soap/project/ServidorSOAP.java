/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package soap.project;

import java.security.SecureRandom;

import javax.jws.WebService;

/**
 *
 * @author 20171014040001
 */

@WebService(endpointInterface = "soap.project.SOAPInterface")
public class ServidorSOAP implements SOAPInterface{
    // Definição dos caracteres possíveis
    private static final String LETRAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    private static final String NUMEROS = "0123456789";
    private static final String CARACTERES_ESPECIAIS = "!@#$%^&*()-_=+[]{}|;:,.<>?";

    @Override
    public String olaMundo(String nome) {
        System.out.println("OLÁ MUNDO ACESSADA..");
        return "OLÁ MUNDO: " + nome;    
    }

    private SecureRandom random = new SecureRandom();
    
    @Override
    public String gerarSenha(int comprimento, boolean incluirNumeros, boolean incluirCaracteresEspeciais) {
        StringBuilder caracteresPermitidos = new StringBuilder(LETRAS);

        if (incluirNumeros) {
            caracteresPermitidos.append(NUMEROS);
        }

        if (incluirCaracteresEspeciais) {
            caracteresPermitidos.append(CARACTERES_ESPECIAIS);
        }

        if (caracteresPermitidos.length() == 0 || comprimento <= 0) {
            throw new IllegalArgumentException("Parâmetros inválidos para geração de senha.");
        }

        StringBuilder senha = new StringBuilder(comprimento);
        for (int i = 0; i < comprimento; i++) {
            int index = random.nextInt(caracteresPermitidos.length());
            senha.append(caracteresPermitidos.charAt(index));
        }

        return senha.toString();
    }
}

