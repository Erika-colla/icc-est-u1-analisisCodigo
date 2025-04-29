import java.util.Random;

public class Benchmarking {

    private MetodosOrdenamiento metodosOrdenamiento;

    public Benchmarking(){

        long inicioMillis = System.currentTimeMillis();
        long inicioNano= System.nanoTime();
        System.out.println(inicioMillis);
        System.out.println(inicioNano);

        metodosOrdenamiento=new MetodosOrdenamiento();
        int [] arreglo=generarArregloAleatorio(1000000);
        Runnable tarea=()-> metodosOrdenamiento.burbujaTradicional(arreglo);

        double tiempoNano=medirConNanoTime(tarea);
        double tiempoMillis=medirConCurrentTime(tarea);
        System.out.println("Tiempo con NanoTime "+tiempoNano +" segundos");
        System.out.println("Tiempo con Millis "+tiempoMillis+ "segundos");

    }
    private int[] generarArregloAleatorio(int n) {
        int[] arreglo = new int[n];
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            arreglo[i] = random.nextInt(10000);
        }
        return arreglo;
    }

    public double medirConNanoTime(Runnable tarea){
        long inicio= System.nanoTime();
        tarea.run();
        long fin=System.nanoTime();
        return (fin-inicio)/1_000_000_000.0;

    }

    public double medirConCurrentTime(Runnable tarea){
        long inicio =System.currentTimeMillis();
        tarea.run();
        long fin=System.currentTimeMillis();
        return (fin-inicio)/1000;

    }

}