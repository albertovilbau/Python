import cs1.*;

public class Principal{

   private static int[][] guardaroctetos(String texto, int numoctetos){
   
      int octetos[][] = new int [numoctetos][8];
      char numero;
      int fila = 0, columna = 0, digito;
      
      //Con este for recorremos el texto introducido y lo vamos pasando a INT, a su vez lo guardamos en el array.
      for(int i = 0; i < texto.length(); i++){
         numero = texto.charAt(i);
         
         digito = Character.getNumericValue(numero);
         
         octetos[columna][fila] = digito;
         fila++;
         if(fila == 8){
            fila = 0;
            columna++;
         }
      }
      
      return octetos;   
   
   }
   
   private static int[] transformaroctetos (int[][] octetos, int numoctetos){
      
      int sumatotal;
      int binariosenteros[] = new int [numoctetos];
      
      //Comprobamos cada posicion del array, si es un 1 le sumamos el valor correspondiente en funcion de su posicion
      for (int i = 0; i < numoctetos; i++){
         
         sumatotal = 0;
         
         if(octetos[i][0] == 1){
            sumatotal = sumatotal + 128;
         }
         if(octetos[i][1] == 1){
            sumatotal = sumatotal + 64;
         }
         if(octetos[i][2] == 1){
            sumatotal = sumatotal + 32;
         }
         if(octetos[i][3] == 1){
            sumatotal = sumatotal + 16;
         }
         if(octetos[i][4] == 1){
            sumatotal = sumatotal + 8;
         }
         if(octetos[i][5] == 1){
            sumatotal = sumatotal + 4;
         }
         if(octetos[i][6] == 1){
            sumatotal = sumatotal + 2;
         }
         if(octetos[i][7] == 1){
            sumatotal = sumatotal + 1;
         }
           
         binariosenteros[i] = sumatotal;
           
      }
      
      return binariosenteros;
      
   }
   
   private static String enterosToString (int[] binariosenteros){
      
      String frasefinal = "";
      
      //Transformamos el contenido del array de int a char, y lo concatenamos todo junto en un string.
      for(int i = 0; i < binariosenteros.length;i++){
         
         frasefinal = frasefinal + (char)(binariosenteros[i]);
           
      }
      
      return frasefinal;
      
   }
   
   private static int[] stringToInt (String texto, int[] letrasenteras){
      
      char posicio;
      
    //Este for, nos permite coger cada letra y convertirla a INT en su valor de la tabla ASCII
      for(int i = 0;i < texto.length();i++){
            
         posicio = texto.charAt(i);
            
         letrasenteras[i] = (int)(posicio);
      }
      
      return letrasenteras;
   
   }
      
   private static int[][] intToBinario (int[][] codigo, int[] letrasenteras){
   
      int entero;
      
      for (int j = 0; j < letrasenteras.length; j++){
         entero = letrasenteras[j];
               
         if(entero >= 128){
            codigo[j][0] = 1;
            entero = entero - 128;
         }
         if(entero >= 64){
            codigo[j][1] = 1;
            entero = entero - 64;
         }
         if(entero >= 32){
            codigo[j][2] = 1;
            entero = entero - 32;
         }
         if(entero >= 16){
            codigo[j][3] = 1;
            entero = entero - 16;
         }
         if(entero >= 8){
            codigo[j][4] = 1;
            entero = entero - 8;
         }
         if(entero >= 4){
            codigo[j][5] = 1;
            entero = entero - 4;
         }
         if(entero >= 2){
            codigo[j][6] = 1;
            entero = entero - 2;
         }
         if(entero >= 1){
            codigo[j][7] = 1;
            entero = entero - 1;
         }
      }
      
      return codigo;
   
   }

   public static void main (String[] args){
   
      String texto, frasefinal, opcion;
      int numoctetos;
      
      do{
      //MENU
      System.out.printf("%nOpcion a escoger: %n");
      System.out.printf("A: Convertir TEXTO a BINARIO%n");
      System.out.printf("B: Convertir BINARIO a TEXTO%n");
      System.out.printf("C: Salir%n");
      System.out.printf("Opcion: ");
      opcion = Keyboard.readString();
      
      if(opcion.equals("A")){
         
         //Pedimos al usuario que introduzca el texto a traducir
         System.out.printf("Texto a traducir: ");
         texto = Keyboard.readString();
         
         //Creamos un array para guardar el valor de cada letra en la tabla ascii
         int letrasenteras[] = new int [texto.length()];
      
         letrasenteras = stringToInt(texto, letrasenteras);
         
         //Creamos otro array que pasa los numeros enteros a octetos binarios. 
         int codigo[][] = new int [letrasenteras.length][8];
         
         codigo = intToBinario(codigo, letrasenteras);
         
         //Mostramos el codigo binario por pantalla
         System.out.printf("Codigo: ");
         
         for(int i = 0;i < letrasenteras.length; i++){
            for(int j = 0; j < 8; j++){
               System.out.printf("%d", codigo[i][j]);
            }
         }
      
      }else if(opcion.equals("B")){
      
      //Pedimos al usuario que nos introduzca el codigo binario.
         System.out.printf("Binario a traducir: ");
         texto = Keyboard.readString();
      
      //Dividimos el codigo binario entre 8 para saber el numero de octetos que tenemos.
         texto = texto.trim();
         numoctetos = texto.length()/8;
      
      //Creamos 2 arrays, uno para guardar los octetos y otro para guardar los octetos cuando sean numeros enteros. 
         int octetos[][] = new int [numoctetos][8];
         int binariosenteros[] = new int [numoctetos];
      
      //Mandamos el texto introducido por el usuario a la funcion y nos devuelve un array 2D con los octetos divididos.
         octetos = guardaroctetos(texto, numoctetos); 
       
      //Mandamos el array a la funcion para que nos devuelva otro array con los numeros binarios pasados a enteros. 
         binariosenteros = transformaroctetos(octetos,numoctetos);
      
      //Mandamos el array a la funcion y nos devuelve el resultado en formato String. (Transformado mediante la tabla ASCII).     
         frasefinal = enterosToString(binariosenteros);
      
         System.out.printf("%s", frasefinal);
      }else if(!opcion.equals("C")){
         System.out.printf("ERROR");
      }
      }while(!opcion.equals("C"));
      
   }

}