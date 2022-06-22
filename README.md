# trees-everywhere
application for registering places, where you can plant a tree


cadastrar 2 usuaários ok

cadastrar 2 contas ok

cada usuário em respectivas contas ok 

cadastrar 2 plants em cada usuário ok

visualizar os filtros ok

_

4 em cada

misturar a conta



  wp:
    image: nginx-trees:1.0
    container_name: nginx-trees
    build: 
      context: .
      dockerfile: Dockerfile.ng
    volumes:
      - static_volume:/deploy/apps/trees-everywhere/app/interface/static_files
      - ./env/nginx:/deploy/apps/trees-everywhere/env/nginx
    ports:
      - 8002:80
    depends_on:
      - app
volumes:
  static_volume:
  pg-data-treeseverywhere: