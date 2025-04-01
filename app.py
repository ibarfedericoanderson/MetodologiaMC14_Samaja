import streamlit as st
import streamlit.components.v1 as components

# HTML simplificado con el diagrama Mermaid y tooltips usando Tippy.js
html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diagrama de Flujo - Metodología de Investigación</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: white;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            width: 100%;
            max-width: 1900px;
            padding: 20px;
            box-sizing: border-box;
            position: relative;
        }
        
        /* Estilos para tooltips personalizados */
        .custom-tooltip {
            position: absolute;
            background-color: rgba(0, 0, 0, 0.9);
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
            font-size: 14px;
            line-height: 1.4;
            max-width: 400px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            z-index: 1000;
            display: none;
            pointer-events: none;
            transition: opacity 0.3s;
        }
        
        .custom-tooltip h3 {
            margin-top: 0;
            color: #ffb74d;
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            padding-bottom: 5px;
        }
        
        .custom-tooltip p {
            margin: 5px 0;
        }
        
        /* Estilos específicos para los nodos del diagrama */
        .inicio circle {
            fill: #9ccc65;
            stroke: #7cb342;
            stroke-width: 1px;
        }
        .instancia .label-container {
            fill: #ffb74d;
            stroke: #ff9800;
            stroke-width: 1px;
        }
        .fase .label-container {
            fill: #90caf9;
            stroke: #2196f3;
            stroke-width: 1px;
        }
        .momento circle {
            fill: #f48fb1;
            stroke: #e91e63;
            stroke-width: 1px;
        }
        .decision .label-container {
            fill: #ffcccc;
            stroke: #cc0000;
            stroke-width: 1px;
        }
        .datos .label-container {
            fill: #ccffff;
            stroke: #008888;
            stroke-width: 1px;
        }
        .documento .label-container {
            fill: #ffccff;
            stroke: #880088;
            stroke-width: 1px;
        }
        
        /* Estilos para hacer que los nodos se destaquen al pasar el ratón */
        .node:hover {
            filter: brightness(1.2);
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <pre class="mermaid">
        %%{
            init: {
                'theme': 'base',
                'themeVariables': {
                    'primaryColor': '#ffffff',
                    'primaryTextColor': '#000000',
                    'primaryBorderColor': '#ffffff',
                    'lineColor': '#ffffff',
                    'secondaryColor': '#006100',
                    'tertiaryColor': '#121212'
                }
            }
        }%%
        
        flowchart TB
            %% Definición de estilos
            classDef inicio fill:#9ccc65,stroke:#7cb342,stroke-width:1px
            classDef instancia fill:#ffb74d,stroke:#ff9800,stroke-width:1px
            classDef fase fill:#90caf9,stroke:#2196f3,stroke-width:1px
            classDef momento fill:#f48fb1,stroke:#e91e63,stroke-width:1px
            classDef decision fill:#ffcccc,stroke:#cc0000,stroke-width:1px
            classDef datos fill:#ccffff,stroke:#008888,stroke-width:1px
            classDef documento fill:#ffccff,stroke:#880088,stroke-width:1px
            
            %% Símbolos de inicio y fin según ISO 5807
            Start((INICIO)) ---> A
            
            %% Nodo principal
            A[Proceso de Investigación Científica] ---> B
            
            %% Instancias principales - Hexágonos según ISO 5807
            B{{1. INSTANCIA DE VALIDACIÓN CONCEPTUAL}} ---> C
            B ---> D
            E{{2. INSTANCIA DE VALIDACIÓN EMPÍRICA}} ---> F
            E ---> G
            H{{3. INSTANCIA DE VALIDACIÓN OPERATIVA}} ---> I
            H ---> J
            K{{4. INSTANCIA DE VALIDACIÓN EXPOSITIVA}} ---> L
            K ---> M
            
            %% Fase 1 y momentos - Paralelogramos para fases
            C[/Fase 1: Planteamientos/] ---> C1
            C ---> C2
            C ---> C3
            C ---> C4
            C1([a. Examen de problemas]) ---> CM
            C2([b. Conocimientos previos]) ---> CM
            C3([c. Relaciones lógicas]) ---> CM
            C4([d. Objetivos]) ---> CM
            CM{Examen de problemas<br>Conocimientos previos<br>Relaciones lógicas<br>Objetivos}
            
            %% Fase 2 y momentos
            D[/Fase 2: Formulación/] ---> D1
            D ---> D2
            D ---> D3
            D ---> D4
            D1([a. Formulación del problema]) ---> DM
            D2([b. Hipótesis sustantivas]) ---> DM
            D3([c. Marco teórico]) ---> DM
            D4([d. Formulación de objetivos]) ---> DM
            DM{Hipótesis sustantivas<br>Marco teórico<br>Modelo del objeto<br>Consecuencias contrastables}
            
            %% Fase 3 y momentos
            F[/Fase 3: Diseño del objeto/] ---> F1
            F ---> F2
            F ---> F3
            F ---> F4
            F1([a. Análisis de estructura]) ---> FM
            F2([b. Análisis de hipótesis]) ---> FM
            F3([c. Fuentes de datos]) ---> FM
            F4([d. Dimensiones de variables]) ---> FM
            FM[(Definición de<br>matriz de datos:<br>UA, V)]
            
            %% Fase 4 y momentos
            G[/Fase 4: Diseño de procedimientos/] ---> G1
            G ---> G2
            G ---> G3
            G ---> G4
            G1([a. Muestras posibles]) ---> GM
            G2([b. Plan de tratamiento]) ---> GM
            G3([c. Recursos y contextos]) ---> GM
            G4([d. Diseño de instrumentos]) ---> GM
            GM[(Operacionalización:<br>I, R)]
            
            %% Fase 5 y momentos
            I[/Fase 5: Recolección y procesamiento/] ---> I1
            I ---> I2
            I ---> I3
            I ---> I4
            I1([a. Pruebas piloto]) ---> IM
            I2([b. Recolección]) ---> IM
            I3([c. Procesamiento]) ---> IM
            I4([d. Tabulación]) ---> IM
            IM[(Llenado de<br>matriz de datos)]
            
            %% Fase 6 y momentos
            J[/Fase 6: Tratamiento y análisis/] ---> J1
            J ---> J2
            J ---> J3
            J ---> J4
            J1([a. Discusión de resultados]) ---> JM
            J2([b. Análisis estadístico]) ---> JM
            J3([c. Interpretación]) ---> JM
            J4([d. Conclusiones]) ---> JM
            JM[(Análisis de<br>matriz de datos)]
            
            %% Fase 7 y momentos
            L[/Fase 7: Informes parciales/] ---> L1
            L ---> L2
            L ---> L3
            L ---> L4
            L1([a. Evaluación del período]) ---> LM
            L2([b. Evaluación de resultados]) ---> LM
            L3([c. Nuevos problemas]) ---> LM
            L4([d. Sugerencias]) ---> LM
            LM>Comunicación<br>de avances]
            
            %% Fase 8 y momentos
            M[/Fase 8: Exposición sistemática/] ---> M1
            M ---> M2
            M ---> M3
            M ---> M4
            M ---> M5
            M ---> M6
            M1([a. Destinatarios]) ---> MM
            M2([b. Ordenamiento de tesis]) ---> MM
            M3([c. Desarrollo de argumentos]) ---> MM
            M4([d. Redacción]) ---> MM
            M5([e. Revisión]) ---> MM
            M6([f. Publicación]) ---> MM
            MM>Informe<br>final]
            
            %% Símbolo de fin
            MM ---> End((FIN))
            
            %% Conexiones entre fases
            CM ---> D
            DM ---> E
            FM ---> G
            GM ---> H
            IM ---> J
            JM ---> K
            LM ---> M
            
            %% Aplicación de estilos
            class Start,End inicio
            class B,E,H,K instancia
            class C,D,F,G,I,J,L,M fase
            class CM,DM decision
            class FM,GM,IM,JM datos
            class LM,MM documento
            class C1,C2,C3,C4,D1,D2,D3,D4,F1,F2,F3,F4,G1,G2,G3,G4,I1,I2,I3,I4,J1,J2,J3,J4,L1,L2,L3,L4,M1,M2,M3,M4,M5,M6 momento
            
            %% Cambiar todas las flechas del diagrama principal a blanco
            linkStyle default stroke:#ffffff,stroke-width:2px
            
            %% Leyenda con colores y símbolos ISO correctos y flechas blancas punteadas
            Z0((Inicio)) -.->|" "| Z1{{Instancia de Validación}}
            Z1 -.->|" "| Z2[/Fase/]
            Z2 -.->|" "| Z3([Momento])
            Z3 -.->|" "| Z4[(Matriz de Datos)]
            Z4 -.->|" "| Z5>Informes]
            Z5 -.->|" "| Z7((Fin))
            
            %% Las flechas de la leyenda también serán blancas por defecto
            
            class Z0,Z7 inicio
            class Z1 instancia
            class Z2 fase
            class Z3 momento
            class Z4 datos
            class Z5 documento
        </pre>
    </div>

    <script>
        // Configuración de Mermaid
        mermaid.initialize({
            startOnLoad: true,
            theme: 'default',
            securityLevel: 'loose',
            flowchart: {
                useMaxWidth: false,
                htmlLabels: true,
                curve: 'basis'
            },
            themeVariables: {
                fontSize: '16px',
                arrowheadColor: '#ffffff',
                lineColor: '#ffffff'
            }
        });
        
        // Datos para los tooltips
        const tooltipData = {
            // Instancias
            'B': {
                title: '1. INSTANCIA DE VALIDACIÓN CONCEPTUAL',
                content: 'Esta instancia tiene como objetivo validar las hipótesis sustantivas por referencia a las teorías y hechos que se consideran bien establecidos.'
            },
            'E': {
                title: '2. INSTANCIA DE VALIDACIÓN EMPÍRICA',
                content: 'Esta instancia está encargada de validar las hipótesis instrumentales o indicadoras, lo que tradicionalmente se conoce como "establecer la validez de los datos".'
            },
            'H': {
                title: '3. INSTANCIA DE VALIDACIÓN OPERATIVA',
                content: 'Esta instancia está encargada de validar las hipótesis operativas o de generalización, lo que tradicionalmente se conoce como "establecer la confiabilidad de los datos y la confiabilidad de la muestra".'
            },
            'K': {
                title: '4. INSTANCIA DE VALIDACIÓN EXPOSITIVA',
                content: 'Esta instancia está encargada de validar las hipótesis retóricas, esto es, el esquema expositivo y la estrategia de argumentación o de exposición demostrativa.'
            },
            
            // Fases
            'C': {
                title: 'Fase 1: Planteamientos',
                content: 'El objeto general de esta fase es familiarizarse y profundizar el conocimiento del proceso en el que se presenta el problema, además de confirmar el interés o importancia de dicho proceso para justificar el esfuerzo de investigación.'
            },
            'D': {
                title: 'Fase 2: Formulación',
                content: 'El objeto central de la fase formulativa es el de lograr las definiciones conceptuales y los análisis de las estructuras de las redes conceptuales implícitas en el problema, en las hipótesis, en el marco teórico y en los objetivos.'
            },
            'F': {
                title: 'Fase 3: Diseño del objeto',
                content: 'El objeto general de esta fase es decidir cuál será el objeto empírico de la investigación. Esto implica escoger los tipos de unidades de análisis, las variables y las fuentes que se emplearán en el estudio.'
            },
            'G': {
                title: 'Fase 4: Diseño de procedimientos',
                content: 'Esta fase tiene como objeto la toma de decisiones acerca de los procedimientos mediante los que se determinarán las unidades de análisis, las dimensiones de las variables, los indicadores y el tratamiento que se les dará a los datos.'
            },
            'I': {
                title: 'Fase 5: Recolección y procesamiento',
                content: 'Esta fase tiene como objetivo llevar a cabo la recolección de los datos y su procesamiento. El investigador debe justificar cómo procedió para seleccionar cada sujeto de estudio y cómo efectuó las mediciones.'
            },
            'J': {
                title: 'Fase 6: Tratamiento y análisis de datos',
                content: 'Esta fase tiene como objeto la discusión y la interpretación de los datos a la luz del plan de análisis y de las hipótesis formuladas (tanto sustantivas, como de validez y de generalización).'
            },
            'L': {
                title: 'Fase 7: Informes parciales',
                content: 'El objetivo de esta fase es organizar y presentar informes parciales sobre los avances de la investigación, incluyendo la evaluación del período, resultados parciales y análisis de nuevos problemas.'
            },
            'M': {
                title: 'Fase 8: Exposición sistemática',
                content: 'El objetivo general de esta última fase consiste en exponer los resultados obtenidos tal como se piensa que ellos se incorporan al cuerpo teórico principal del cual se ha partido.'
            },
            
            // Momentos - Fase 1
            'C1': {
                title: 'a. Examen de problemas',
                content: 'Examen y discusión de los problemas (el problema central y los problemas conexos). Palabra clave: "Problema".'
            },
            'C2': {
                title: 'b. Conocimientos previos',
                content: 'Examen y discusión de las hipótesis que evocan los problemas. Palabra clave: "Hipótesis".'
            },
            'C3': {
                title: 'c. Relaciones lógicas',
                content: 'Apropiación y revisión de los conocimientos previos, propios o análogos. Palabra clave: "Teorías".'
            },
            'C4': {
                title: 'd. Objetivos',
                content: 'Revisión y discusión sobre los contextos materiales e institucionales de los problemas. Palabra clave: "Propósitos".'
            },
            
            // Momentos - Fase 2
            'D1': {
                title: 'a. Formulación del problema',
                content: 'Formulación precisa del problema central y de los problemas derivados. Palabra clave: "Problema".'
            },
            'D2': {
                title: 'b. Hipótesis sustantivas',
                content: 'Formulación de las hipótesis sustantivas y de las hipótesis auxiliares. Palabra clave: "Hipótesis".'
            },
            'D3': {
                title: 'c. Marco teórico',
                content: 'Formulación del marco teórico o modelo conceptual. Palabra clave: "Teoría".'
            },
            'D4': {
                title: 'd. Formulación de objetivos',
                content: 'Formulación de los objetivos teóricos y prácticos. Palabra clave: "Propósitos".'
            },
            
            // Momentos - Fase 3
            'F1': {
                title: 'a. Análisis de estructura',
                content: 'Análisis estructural del objeto a investigar. Palabra clave: "Estructura".'
            },
            'F2': {
                title: 'b. Análisis de hipótesis',
                content: 'Análisis de las hipótesis y determinación de las variables. Palabra clave: "Variables".'
            },
            'F3': {
                title: 'c. Fuentes de datos',
                content: 'Delimitación de las fuentes de datos para cada variable. Palabra clave: "Fuentes".'
            },
            'F4': {
                title: 'd. Dimensiones de variables',
                content: 'Determinación de las dimensiones de las variables complejas. Palabra clave: "Dimensiones".'
            },
            
            // Momentos - Fase 4
            'G1': {
                title: 'a. Muestras posibles',
                content: 'Diseño del muestreo para cada tipo de unidad de análisis. Palabra clave: "Muestra".'
            },
            'G2': {
                title: 'b. Plan de tratamiento',
                content: 'Planificación del tratamiento que se dará a los datos. Palabra clave: "Tratamiento".'
            },
            'G3': {
                title: 'c. Recursos y contextos',
                content: 'Determinación de recursos y contextos de tiempo y lugar. Palabra clave: "Recursos".'
            },
            'G4': {
                title: 'd. Diseño de instrumentos',
                content: 'Diseño de instrumentos para la recolección de datos. Palabra clave: "Instrumentos".'
            },
            
            // Momentos - Fase 5
            'I1': {
                title: 'a. Pruebas piloto',
                content: 'Pruebas piloto de los instrumentos y entrenamiento del equipo. Palabra clave: "Piloto".'
            },
            'I2': {
                title: 'b. Recolección',
                content: 'Recolección de los datos mediante los instrumentos diseñados. Palabra clave: "Recolección".'
            },
            'I3': {
                title: 'c. Procesamiento',
                content: 'Procesamiento y agrupamiento de los datos recolectados. Palabra clave: "Procesamiento".'
            },
            'I4': {
                title: 'd. Tabulación',
                content: 'Tabulación y desarrollo de la matriz de datos. Palabra clave: "Tabulación".'
            },
            
            // Momentos - Fase 6
            'J1': {
                title: 'a. Discusión de resultados',
                content: 'Discusión colectiva de los primeros resultados obtenidos. Palabra clave: "Discusión".'
            },
            'J2': {
                title: 'b. Análisis estadístico',
                content: 'Análisis estadístico de los datos según el plan de análisis. Palabra clave: "Estadística".'
            },
            'J3': {
                title: 'c. Interpretación',
                content: 'Interpretación sustantiva de los resultados estadísticos. Palabra clave: "Interpretación".'
            },
            'J4': {
                title: 'd. Conclusiones',
                content: 'Elaboración de conclusiones en relación con las hipótesis. Palabra clave: "Conclusiones".'
            },
            
            // Momentos - Fase 7
            'L1': {
                title: 'a. Evaluación del período',
                content: 'Evaluación de lo realizado en el período. Palabra clave: "Evaluación".'
            },
            'L2': {
                title: 'b. Evaluación de resultados',
                content: 'Evaluación de los resultados obtenidos hasta el momento. Palabra clave: "Resultados".'
            },
            'L3': {
                title: 'c. Nuevos problemas',
                content: 'Análisis de los nuevos problemas surgidos durante la investigación. Palabra clave: "Problemas".'
            },
            'L4': {
                title: 'd. Sugerencias',
                content: 'Sugerencias para el período siguiente de investigación. Palabra clave: "Sugerencias".'
            },
            
            // Momentos - Fase 8
            'M1': {
                title: 'a. Destinatarios',
                content: 'Determinación de los destinatarios del informe final. Palabra clave: "Audiencia".'
            },
            'M2': {
                title: 'b. Ordenamiento de tesis',
                content: 'Ordenamiento de las tesis y conclusiones principales. Palabra clave: "Tesis".'
            },
            'M3': {
                title: 'c. Desarrollo de argumentos',
                content: 'Desarrollo de los argumentos que apoyan cada tesis. Palabra clave: "Argumentos".'
            },
            'M4': {
                title: 'd. Redacción',
                content: 'Redacción del borrador del informe final. Palabra clave: "Redacción".'
            },
            'M5': {
                title: 'e. Revisión',
                content: 'Revisión crítica del borrador por parte del equipo. Palabra clave: "Revisión".'
            },
            'M6': {
                title: 'f. Publicación',
                content: 'Ajustes y publicación del informe final. Palabra clave: "Publicación".'
            },
            
            // Elementos especiales
            'CM': {
                title: 'Síntesis de la Fase 1',
                content: 'Integración de los conocimientos sobre el problema, hipótesis, teorías y propósitos de la investigación.'
            },
            'DM': {
                title: 'Síntesis de la Fase 2',
                content: 'Consolidación del marco teórico, las hipótesis, el modelo conceptual del objeto y las consecuencias observables de las hipótesis.'
            },
            'FM': {
                title: 'Matriz de datos: UA, V',
                content: 'Definición de la matriz de datos, incluyendo las unidades de análisis (UA) y las variables (V) que serán estudiadas.'
            },
            'GM': {
                title: 'Operacionalización: I, R',
                content: 'Operacionalización de las variables a través de indicadores (I) y procedimientos o reglas (R) para la medición.'
            },
            'IM': {
                title: 'Llenado de matriz de datos',
                content: 'Completar la matriz de datos con la información recolectada y procesada.'
            },
            'JM': {
                title: 'Análisis de matriz de datos',
                content: 'Análisis estadístico y conceptual de la matriz de datos completada, para extraer conclusiones validadas.'
            },
            'LM': {
                title: 'Comunicación de avances',
                content: 'Elaboración y presentación de informes parciales sobre el progreso de la investigación.'
            },
            'MM': {
                title: 'Informe final',
                content: 'Documento final de la investigación que integra todos los elementos del proceso investigativo en un formato adecuado para su difusión académica.'
            }
        };
        // Creamos un div para el tooltip
        const tooltipDiv = document.createElement('div');
        tooltipDiv.className = 'custom-tooltip';
        document.body.appendChild(tooltipDiv);
        
        // Función para inicializar eventos de tooltip
        function initTooltips() {
            console.log('Inicializando tooltips');
            
            // Esperamos a que Mermaid termine de renderizar
            setTimeout(() => {
                // Obtener todos los nodos del diagrama
                const nodes = document.querySelectorAll('.node');
                console.log('Nodos encontrados:', nodes.length);
                
                nodes.forEach(node => {
                    // Extraer el ID del nodo simplificado para buscar en nuestros datos
                    const nodeIdFull = node.id;
                    const nodeId = nodeIdFull.replace('flowchart-', '').split('-')[0];
                    
                    // Verificar si tenemos datos para este nodo
                    if (tooltipData[nodeId]) {
                        // Añadir eventos de ratón
                        node.addEventListener('mouseover', function(e) {
                            const data = tooltipData[nodeId];
                            
                            // Contenido HTML para el tooltip
                            tooltipDiv.innerHTML = `
                                <h3>${data.title}</h3>
                                <p>${data.content}</p>
                            `;
                            
                            // Posicionamos el tooltip cerca del cursor
                            tooltipDiv.style.left = (e.pageX + 15) + 'px';
                            tooltipDiv.style.top = (e.pageY + 15) + 'px';
                            
                            // Mostramos el tooltip
                            tooltipDiv.style.display = 'block';
                            
                            console.log('Mostrando tooltip para:', nodeId);
                        });
                        
                        // Seguir el cursor
                        node.addEventListener('mousemove', function(e) {
                            tooltipDiv.style.left = (e.pageX + 15) + 'px';
                            tooltipDiv.style.top = (e.pageY + 15) + 'px';
                        });
                        
                        // Ocultar el tooltip al quitar el ratón
                        node.addEventListener('mouseout', function() {
                            tooltipDiv.style.display = 'none';
                        });
                    }
                });
            }, 3000); // Damos tiempo suficiente para que el diagrama se renderice
        }
        
        // Iniciamos los tooltips cuando la página esté lista
        document.addEventListener('DOMContentLoaded', initTooltips);
        
        // También intentamos inicializar cuando todos los recursos estén cargados
        window.addEventListener('load', initTooltips);
        
        // Y para mayor seguridad, iniciamos después de un tiempo fijo
        setTimeout(initTooltips, 5000);
    </script>
</body>
</html>
"""

def main():
    # Configuración de la página
    st.set_page_config(
        page_title="Diagrama de Flujo Interactivo - Metodología de Investigación",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Información del autor
    st.markdown("""
    <div style='background-color: #2D2D2D; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
        <h2 style='color: white;'>👤 Autor</h2>
        <p style='color: white;'>© 2025 <strong>Ibar Federico Anderson, Ph.D., Master, Industrial Designer</strong></p>
        <div style='display: flex; justify-content: space-between; margin-top: 10px;'>
            <div>
                <p style='color: white;'><img src="https://upload.wikimedia.org/wikipedia/commons/c/c7/Google_Scholar_logo.svg" style="height: 20px; vertical-align: middle;"> <a href="https://scholar.google.com/citations?user=mXD4RFUAAAAJ&hl=en" target="_blank" style='color: white;'>Google Scholar</a></p>
                <p style='color: white;'><img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" style="height: 20px; vertical-align: middle;"> <a href="https://orcid.org/0000-0002-9732-3660" target="_blank" style='color: white;'>ORCID</a></p>
            </div>
            <div>
                <p style='color: white;'><img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/ResearchGate_icon_SVG.svg" style="height: 20px; vertical-align: middle;"> <a href="https://www.researchgate.net/profile/Ibar-Anderson" target="_blank" style='color: white;'>Research Gate</a></p>
                <p style='color: white;'><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" style="height: 20px; vertical-align: middle;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" style="height: 20px; vertical-align: middle;"> <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" style='color: white;'>CC BY 4.0 License</a></p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Título ISO 5807
    st.markdown("""
    <h3 style='text-align: center; color: black;'>Diagrama de flujo basado en la norma <strong>ISO 5807:1985</strong></h3>
    """, unsafe_allow_html=True)

    # Ocultamos elementos de la interfaz de Streamlit
    st.markdown("""
    <style>
        .css-18e3th9 {
            padding-top: 0;
            padding-bottom: 0;
        }
        .css-1d391kg {
            padding-top: 0;
            padding-bottom: 0;
        }
        footer {
            display: none;
        }
        header {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

    # Renderizar la página completa con el diagrama
    components.html(html, height=1200, scrolling=True)

if __name__ == "__main__":
    main()