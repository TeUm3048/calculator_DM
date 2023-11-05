# Гайд "Как собрать ~~вещи на~~ фронт" или "Как начать писать HTML"

## Шаг 1. Устанавливаем Node.js v18

Слишком много вариантов: бинарники, пакетные менеджеры, докер, специальные менеджеры версий ноды.

- [Страничка с бинарниками под винду и другие системы](https://nodejs.org/download/release/latest-v18.x/)
- Если вы предпочитаете пакетные менеджеры, устанавливаем через них — [тысяча и один пример](https://nodejs.org/download/release/latest-v18.x/)

## Шаг 2. Устанавливаем пакетный менеджер yarn

Почему [yarn](https://yarnpkg.com/getting-started)? — потому что.

Начнём с включения [Corepack](https://nodejs.org/dist/latest/docs/api/corepack.html), если он еще не включен:

```bash
corepack enable
```

Теперь yarn может настроить наш проект и установить зависимости

```
yarn install
```

## Шаг 3. Собираем проект

Запустить в режиме разработки:

```bash
yarn dev
```

Собрать проект для прода:

```bash
yarn build
```

Чтобы запусить бекэнд сервер, читайте [гайд django](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
