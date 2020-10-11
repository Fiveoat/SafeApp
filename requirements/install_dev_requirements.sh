if [ "$DEV" == "true" ]; then
  pip --use-feature=2020-resolver install --user -r ./requirements/requirements-dev.txt
fi
