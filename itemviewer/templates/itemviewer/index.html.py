{% if summoners_list %}
    <ul>
    {% for summoner in summoner_list %}
        <li>
            <a href="/itemviewer/{{ summoner.summoner_id }}/">
                {{ summoner.summoner_name }}
            </a>
        </li>
    {% endfor %}
    </ul>
{% else %}
    <p>No summoners cached. Search!</p>
{% endif %}
