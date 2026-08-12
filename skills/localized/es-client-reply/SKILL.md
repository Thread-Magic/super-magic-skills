---
name: Respuesta al cliente
description: Redactar una respuesta externa al cliente con la voz y el formato de la casa — actualizaciones de resolución, notas de estado, mensajes de cierre o cualquier correo de cara al cliente sobre un ticket. (Spanish version of Client Reply — drafts on-brand client-facing ticket replies.)
category: Localized
tools: [search_tickets, view_openDraft, add_ticket_note]
connectors: []
scope: single
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Respuesta al cliente

**Cuándo usar:** un técnico necesita enviar un mensaje de cara al cliente y lo quiere alineado con la marca y listo para enviar — una actualización, nota de estado o mensaje de cierre.

**Ejecutar:** en un solo ticket.

## Prompt

```
Redacta una respuesta al cliente lista para enviar en este ticket, con la voz de la casa.

1. Lee primero el hilo completo del ticket — cada mensaje previo, nota y cambio de estado. Nunca redactes solo a partir del último mensaje.
2. Empieza por la respuesta en sí o por el estado actual, y después el detalle de apoyo.
3. Aplica los estándares de voz de la casa:
   - Saluda al cliente por su nombre de pila solo en el primer mensaje del hilo; omite el saludo en las respuestas siguientes del mismo hilo.
   - Sin frases de relleno ("Espero que este correo le encuentre bien", "Me pongo en contacto para..."). Empieza con sustancia.
   - Sin jerga técnica salvo que el cliente haya usado el término primero; si un término técnico es inevitable, añade una explicación en lenguaje llano.
   - 1–2 párrafos cortos. Si necesita más, probablemente necesita una llamada.
4. Si el miembro tiene una lista de palabras preferidas o prohibidas, aplícala: sustituye las palabras prohibidas por sus reemplazos y prioriza las alternativas listadas.
5. Si es una respuesta de cierre, termina el cuerpo con: "Si algo no quedó resuelto, solo tiene que responder a este correo: al responder, el ticket se reabre automáticamente."
6. Firma: si el espacio de trabajo aplica una firma gestionada de forma automática, termina tras la última frase — NO añadas una despedida que quedaría duplicada. Añade despedida solo cuando no exista firma gestionada.
7. Muéstrame la respuesta como borrador abierto para que el técnico la revise, etiquetada como "BORRADOR — revisar antes de enviar". No la envíes.

Convención en español: registro de usted en toda comunicación comercial; si el cliente tutea de forma consistente en el hilo, refleja su registro, pero nunca seas tú quien pase primero al tuteo. Saluda por el nombre de pila aunque trates de usted ("Estimada María:" o "Hola, María:"). Despedidas: "Saludos cordiales" o "Un saludo" (habitual), "Atentamente" (muy formal); evita calcos del inglés ("Mejores saludos"). Muchos clientes usan dos apellidos: no los recortes ni combines. Fechas en texto: "el martes 15 de julio", nunca 07/15; horas en formato de 24 horas.

Salvaguardas: nunca inventes detalles — nada de marcas de tiempo, pasos realizados, números de ticket, enlaces ni promesas fabricadas; si el hilo no establece un hecho, omítelo o márcalo como <confirmar con el técnico>. El borrador sigue siendo borrador hasta que un humano lo apruebe — nunca envíes de forma autónoma. Nunca expongas notas internas, credenciales, precios ni datos de otros clientes. Ajusta el idioma al del cliente. En caso de duda, no hagas nada. Ofrece una nota interna en texto plano si el miembro quiere dejar constancia.
```
