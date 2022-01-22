{% macro create_source_table() -%}

CREATE TABLE IF NOT EXISTS source_data (
    id INTEGER
);

{% endmacro %}
