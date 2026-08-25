---
name: Resumen diario (Spanish)
description: Resumen diario de los tickets abiertos de un técnico: qué espera respuesta, qué es urgente, qué está agendado hoy, con variante ultracorta.
category: Localized
tools: [search_tickets, search_members]
connectors: []
scope: global
flow: no
role: [Technician]
outcome: [Time & Cost Savings (Capacity)]
---

# Resumen diario (Spanish)

**Cuándo usar:** un técnico quiere la lectura de la mañana — todo lo que tiene sobre la mesa, ordenado según lo que le necesita ahora mismo, legible en menos de un minuto. "Dame un resumen de mis tickets abiertos", "resumen de la mañana", "la versión corta".

**Ejecutar:** sobre todos los tickets abiertos del miembro que lo solicita.

## Prompt

```
Genera el resumen diario de los tickets abiertos del miembro que lo pide. Limítalo a sus tickets: nunca incluyas las colas de otros técnicos salvo petición explícita.

1. Recupera todos sus tickets abiertos (resuelve el miembro si hace falta). Si un límite de resultados pudo truncar la lista, dilo al principio ("muestro 50 — puede haber más") en vez de presentarlo como completo.
2. Clasifica cada ticket en un solo bloque, por este orden (gana el primero que encaje):
   - Espera tu respuesta — el cliente respondió el último y espera. Ordena por tiempo de espera.
   - Urgente / en riesgo — prioridad alta, SLA al borde o incumplido, o sentimiento negativo. Ordena por gravedad.
   - Agendado para hoy — con entrada de agenda o seguimiento comprometido, en orden horario.
   - Esperando a terceros — cliente, proveedor o escalación tiene la pelota. Marca los que llevan 3+ días en silencio, sin que este bloque acapare la parte alta.
   - Todo lo demás — solo recuento y una caracterización de una línea.
3. Cada ticket ocupa una línea accionable: número, cliente abreviado, estado en 5–8 palabras y la siguiente acción ("#1234 <cliente> — impresora sin conexión 2 días, respondió ayer → confirmar que el arreglo funciona").
4. Encabeza con "Empieza por aquí:" el ticket más importante y una frase del porqué (la respuesta de cliente que más lleva esperando gana a una urgencia difusa; un SLA incumplido gana a todo).
5. Cierra con la forma del día: totales por bloque y una frase.
6. Si piden la versión corta ("3 líneas"), devuelve exactamente tres líneas, sin encabezados ni preámbulo: (1) Empieza por aquí + el porqué, (2) recuentos — X esperan respuesta / Y urgentes / Z agendados, (3) lo único que te morderá hoy si lo ignoras.
7. Ofrece la continuación: "¿Quieres borradores de respuesta para los que te están esperando?"

Solo lectura: no cambia nada — ni estados, ni notas, ni recordatorios — salvo que lo pidan después. Nunca inventes números de ticket, plazos de SLA ni respuestas de cliente; si la última actividad es ambigua, usa el bloque más seguro (Espera tu respuesta).

Convención en español: fechas en DD/MM/AAAA y, en texto corrido, la fecha completa ("martes 15 de julio") para evitar ambigüedades regionales; horas en 24 h ("a las 14:30"), con el equivalente de 12 h para clientes latinoamericanos ("14:30 / 2:30 p. m."). El resumen se dirige al técnico: tutéalo; reserva el usted para los borradores a clientes. Usa signos de apertura (¿ ¡).

Variante desatendida (Flows — vía Run Skill en un evento de ticket, nunca programado): tu respuesta entera es el briefing, sin narración ni preguntas, siempre con la línea Empieza por aquí y los recuentos, y sin ofrecer continuación. Cola vacía → exactamente: "No tienes tickets abiertos asignados. Disfruta de la bandeja limpia." Búsqueda fallida → una línea diciendo que no pudo generarse, nunca un resumen inventado.
```
