from blueprint import makeApp


app = makeApp()


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

api = os.environ['api_key']