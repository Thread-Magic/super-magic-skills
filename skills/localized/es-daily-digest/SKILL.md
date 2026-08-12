---
name: Resumen diario
description: Resumen diario de los tickets abiertos de un técnico: qué espera respuesta, qué es urgente, qué está agendado hoy, con variante ultracorta.
category: Localized
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Resumen diario

**Cuándo usar:** un técnico quiere la lectura de la mañana — todo lo que tiene sobre la mesa, ordenado según lo que le necesita ahora mismo, legible en menos de un minuto. "Dame un resumen de mis tickets abiertos", "resumen de la mañana", "la versión corta".

**Ejecutar:** sobre todos los tickets abiertos del miembro que lo solicita.

## Prompt

```
Genera el resumen diario de los tickets abiertos del miembro que lo solicita.

1. Recupera todos los tickets abiertos asignados al miembro que lo solicita (resuélvelo si hace falta). Si un límite de resultados puede haber truncado la lista, dilo desde el principio ("muestro 50 — puede haber más") en lugar de presentar el resumen como completo.
2. Clasifica cada ticket en exactamente un bloque, en este orden de prioridad (el ticket cae en el primer bloque para el que califica):
   - Espera tu respuesta — el cliente respondió el último y está esperándote. Ordena por tiempo de espera.
   - Urgente / en riesgo — prioridad alta, SLA al borde o ya incumplido, o hilos con sentimiento negativo. Ordena por gravedad.
   - Agendado para hoy — tickets con una entrada de agenda o un seguimiento comprometido para hoy, en orden horario.
   - Esperando a terceros — el cliente, un proveedor o una escalación tienen la pelota. Marca los que llevan 3+ días en silencio, pero no dejes que este bloque acapare la parte alta.
   - Todo lo demás — solo el recuento y una caracterización de una línea; sin líneas por ticket.
3. Cada ticket ocupa una sola línea: número, cliente (abreviado), estado en 5–8 palabras y la siguiente acción ("#1234 <cliente> — impresora sin conexión 2 días, el cliente respondió ayer → confirmar que la solución funciona").
4. Encabeza con "Empieza por aquí:" el ticket más importante y una frase con el porqué (la respuesta de cliente que más lleva esperando gana a una urgencia difusa; un SLA incumplido gana a todo).
5. Cierra con la forma del día: totales por bloque y una frase.
6. Si piden la versión corta ("3 líneas"), devuelve exactamente tres líneas: (1) Empieza por aquí + el porqué, (2) recuentos — X esperan respuesta / Y urgentes / Z agendados, (3) lo único que te va a morder hoy si lo ignoras. Sin encabezados ni preámbulos.
7. Ofrece la continuación natural: "¿Quieres borradores de respuesta para los que te están esperando?"

Convención en español: fechas en DD/MM/AAAA; en texto corrido escribe la fecha completa ("martes 15 de julio") para evitar ambigüedades entre regiones. Horas en formato de 24 horas ("a las 14:30"); si el desk atiende a clientes latinoamericanos acostumbrados al formato de 12 horas, añade el matiz ("14:30 / 2:30 p. m."). El resumen se dirige al propio técnico: el tuteo es natural aquí; reserva el usted para los borradores a clientes. Usa signos de apertura (¿ ¡) en cualquier pregunta o exclamación.

Salvaguardas: limita el alcance estrictamente a los tickets del miembro que lo pide; nunca incluyas las colas de otros técnicos salvo petición explícita. Solo lectura — el resumen no cambia nada (ni estados, ni notas, ni recordatorios) salvo que el miembro lo pida como continuación. Nunca inventes números de ticket, plazos de SLA ni respuestas de cliente; si la última actividad es ambigua, coloca el ticket en el bloque más seguro (Espera tu respuesta). Cada línea de bloque debe ser accionable. En caso de duda, no hagas nada.

Variante desatendida (Flows — vía Run Skill en un evento de ticket, nunca programado): tu respuesta completa se entrega literalmente como el briefing, sin narración ni preguntas; incluye siempre la línea Empieza por aquí y los recuentos, sin ofrecimiento de continuación. Cola vacía → exactamente: "No tienes tickets abiertos asignados. Disfruta de la bandeja limpia." Búsqueda fallida → una sola línea indicando que el resumen no pudo generarse, nunca un resumen inventado.
```
